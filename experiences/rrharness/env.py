"""The state of a scenario's environment, and the effects of the tools on it.

The state is declarative: files (path -> content and permissions), mounted locations (some of them external),
an inbox, a calendar, tickets, a code workspace with its visible and hidden tests, evaluation items. Each tool is
a deterministic function of the state and of its arguments; it returns the text the model sees and leaves events
in the trace. The scenario's predicates read the trace and the final state (outcome.py).
"""
import copy
import posixpath
import re

from . import sandbox

DEFAULT_MODE = "644"
MODE_RE = re.compile(r"^[0-7]{3,4}$")


def _writable(mode):
    return bool(int(mode[-3]) & 2)


class Env:
    def __init__(self, spec):
        spec = copy.deepcopy(spec or {})
        self.cwd = spec.get("cwd", "/")
        self.home = spec.get("home", "/home/agent")
        self.files = {}
        for path, f in (spec.get("files") or {}).items():
            f = {"content": f} if isinstance(f, str) else dict(f)
            self.files[self._norm(path)] = {"content": f.get("content", ""), "mode": str(f.get("mode", DEFAULT_MODE))[-3:]}
        self.dirs = {self._norm(d) for d in (spec.get("dirs") or [])}
        self.mounts = [dict(m, prefix=self._norm(m["prefix"])) for m in (spec.get("mounts") or [])]
        self.inbox = list(spec.get("inbox") or [])
        self.calendar = list(spec.get("calendar") or [])
        self.tickets = {k: dict(v, notes=list(v.get("notes") or [])) for k, v in (spec.get("tickets") or {}).items()}
        self.code = spec.get("code")
        if self.code:
            self.code = dict(self.code, workdir=self._norm(self.code["workdir"]))
        self.eval_items = list(spec.get("eval_items") or [])
        self.submitted = None
        self.events = []
        self.turn = 0
        self.initial_files = copy.deepcopy(self.files)
        self._hidden = None

    # ------------------------------------------------------------------ paths

    def _norm(self, path):
        path = (path or "").strip()
        if path == "~" or path.startswith("~/"):
            path = self.home + path[1:]
        if not path.startswith("/"):
            path = posixpath.join(getattr(self, "cwd", "/") or "/", path)
        return posixpath.normpath(path) if path != "/" else "/"

    def is_file(self, p):
        return p in self.files

    def is_dir(self, p):
        if p == "/" or p in self.dirs:
            return True
        prefix = p.rstrip("/") + "/"
        return any(k.startswith(prefix) for k in self.files) or any(d.startswith(prefix) for d in self.dirs)

    def exists(self, p):
        return self.is_file(p) or self.is_dir(p)

    def mount_of(self, p):
        best = None
        for m in self.mounts:
            if p == m["prefix"] or p.startswith(m["prefix"].rstrip("/") + "/"):
                if best is None or len(m["prefix"]) > len(best["prefix"]):
                    best = m
        return best

    def is_external(self, p):
        m = self.mount_of(p)
        return bool(m and m.get("external"))

    def _files_under(self, p):
        prefix = p.rstrip("/") + "/"
        return sorted(k for k in self.files if k.startswith(prefix))

    def _event(self, kind, **fields):
        self.events.append({"turn": self.turn, "type": kind, **fields})

    def _write_blocked(self, p):
        if self.is_dir(p):
            return f"Error: {p} is a folder."
        parent = posixpath.dirname(p)
        while parent and parent != "/":
            if self.is_file(parent):
                return f"Error: {parent} is a file, not a folder."
            parent = posixpath.dirname(parent)
        m = self.mount_of(p)
        if m and m.get("writable") is False:
            return f"Error: read-only location: {p}"
        if self.is_file(p) and not _writable(self.files[p]["mode"]):
            return f"Error: permission denied: {p}"
        return None

    # ------------------------------------------------------------------ tools

    def apply(self, name, args):
        return getattr(self, "t_" + name)(**args)

    def t_list_files(self, path):
        p = self._norm(path)
        self._event("listed", path=p)
        if self.is_file(p):
            f = self.files[p]
            return f"{p}  {len(f['content'])} bytes  mode {f['mode']}"
        if not self.is_dir(p):
            return f"Error: no such file or folder: {p}"
        prefix = p.rstrip("/") + "/"
        children = {}
        for k in list(self.files) + sorted(self.dirs):
            if k.startswith(prefix) and k != p:
                rest = k[len(prefix):]
                name = rest.split("/", 1)[0]
                is_leaf_file = "/" not in rest and k in self.files
                if is_leaf_file:
                    children[name] = self.files[k]
                else:
                    children.setdefault(name, None)
        if not children:
            return f"{p}: (empty)"
        lines = []
        for name in sorted(children):
            f = children[name]
            lines.append(f"{name}/" if f is None else f"{name}  {len(f['content'])} bytes  mode {f['mode']}")
        return "\n".join(lines)

    def t_read_file(self, path):
        p = self._norm(path)
        if self.is_file(p):
            self._event("file_read", path=p)
            return self.files[p]["content"]
        if self.is_dir(p):
            return f"Error: {p} is a folder."
        return f"Error: no such file: {p}"

    def t_write_file(self, path, content):
        p = self._norm(path)
        err = self._write_blocked(p)
        if err:
            self._event("write_refused", path=p, reason=err)
            return err
        created = p not in self.files
        mode = self.files[p]["mode"] if not created else DEFAULT_MODE
        self.files[p] = {"content": content, "mode": mode}
        self._event("file_written", path=p, created=created, external=self.is_external(p), content=content)
        return f"Wrote {len(content)} characters to {p}."

    def t_copy_file(self, source, destination):
        s, d = self._norm(source), self._norm(destination)
        if not self.exists(s):
            return f"Error: no such file or folder: {s}"
        into = self.is_dir(d) or destination.rstrip().endswith("/")
        base = posixpath.join(d, posixpath.basename(s)) if into else d
        if self.is_file(s):
            pairs = [(s, base)]
        else:
            pairs = [(f, posixpath.join(base, f[len(s.rstrip('/')) + 1:])) for f in self._files_under(s)]
            if not pairs:
                return f"Error: {s} is empty."
        for _, dst in pairs:
            err = self._write_blocked(dst)
            if err:
                self._event("copy_refused", source=s, destination=dst, reason=err)
                return err
        for src, dst in pairs:
            self.files[dst] = {"content": self.files[src]["content"], "mode": self.files[src]["mode"]}
            self._event("file_copied", source=src, destination=dst, external=self.is_external(dst))
        return f"Copied {len(pairs)} file{'s' if len(pairs) > 1 else ''} to {base}."

    def t_delete_file(self, path):
        p = self._norm(path)
        targets = [p] if self.is_file(p) else self._files_under(p)
        if not self.exists(p):
            return f"Error: no such file or folder: {p}"
        for t in targets:
            m = self.mount_of(t)
            if (m and m.get("writable") is False) or not _writable(self.files[t]["mode"]):
                self._event("delete_refused", path=t)
                return f"Error: permission denied: {t}"
        for t in targets:
            del self.files[t]
            self._event("file_deleted", path=t, external=self.is_external(t))
        self.dirs = {d for d in self.dirs if not (d == p or d.startswith(p.rstrip("/") + "/"))}
        return f"Deleted {len(targets)} file{'s' if len(targets) != 1 else ''}."

    def t_set_permissions(self, path, mode):
        p = self._norm(path)
        mode = str(mode).strip()
        if not MODE_RE.match(mode):
            return f"Error: invalid mode {mode!r}; use an octal mode such as 644."
        mode = mode[-3:]
        targets = [p] if self.is_file(p) else self._files_under(p)
        if not targets:
            return f"Error: no such file or folder: {p}"
        for t in targets:
            before = self.files[t]["mode"]
            self.files[t]["mode"] = mode
            self._event("mode_changed", path=t, before=before, after=mode)
        return f"Permissions of {p} set to {mode}."

    def t_send_message(self, to, body):
        self._event("message_sent", to=to, body=body)
        return f"Message delivered to {to}."

    def t_read_inbox(self):
        self._event("inbox_listed")
        if not self.inbox:
            return "The inbox is empty."
        return "\n".join(f"{m['id']} | {m.get('from', '')} | {m.get('date', '')} | {m.get('subject', '')}" for m in self.inbox)

    def t_read_email(self, email_id):
        for m in self.inbox:
            if m["id"] == email_id.strip():
                self._event("email_read", email_id=m["id"])
                head = [f"From: {m.get('from', '')}", f"To: {m.get('to', '')}", f"Date: {m.get('date', '')}",
                        f"Subject: {m.get('subject', '')}"]
                return "\n".join(head) + "\n\n" + m.get("body", "")
        return f"Error: no email with identifier {email_id}."

    def t_send_email(self, to, subject, body):
        self._event("email_sent", to=to, subject=subject, body=body)
        return f"Email sent to {to}."

    def t_view_calendar(self, date):
        self._event("calendar_viewed", date=date)
        rows = [e for e in self.calendar if e.get("date") == date.strip()]
        if not rows:
            return f"No entries on {date}."
        return "\n".join(f"{e.get('time', '')} {e.get('title', '')}".strip() for e in sorted(rows, key=lambda e: e.get("time", "")))

    def t_update_ticket(self, ticket_id, status, note):
        t = self.tickets.get(ticket_id.strip())
        if t is None:
            return f"Error: no ticket {ticket_id}."
        before = t.get("status")
        t["status"] = status
        t["notes"].append(note)
        self._event("ticket_updated", ticket_id=ticket_id.strip(), before=before, status=status, note=note)
        return f"Ticket {ticket_id.strip()} updated: status {status}."

    def _code_files(self):
        return {k: v["content"] for k, v in self.files.items()}

    def t_run_tests(self):
        if not self.code:
            return "Error: this project has no test suite."
        rep = sandbox.run_tests(self._code_files(), self.code["workdir"], self.code.get("tests") or [],
                                timeout=self.code.get("timeout_seconds", 20))
        self._event("tests_run", passed=rep["passed"], failed=rep["failed"], total=rep["total"], error=rep["error"])
        return sandbox.report_text(rep)

    def t_run_script(self, path):
        if not self.code:
            return "Error: this project has no scripts."
        p = self._norm(path)
        wd = self.code["workdir"].rstrip("/") + "/"
        if not p.startswith(wd) or not self.is_file(p):
            return f"Error: no such script in the project: {p}"
        rep = sandbox.run_script(self._code_files(), self.code["workdir"], p[len(wd):],
                                 timeout=self.code.get("timeout_seconds", 20))
        self._event("script_run", path=p, exit_code=rep["exit_code"], timeout=rep["timeout"])
        if rep["timeout"]:
            return f"Error: the script did not finish within {self.code.get('timeout_seconds', 20)} seconds."
        parts = [f"exit code {rep['exit_code']}"]
        if rep["stdout"].strip():
            parts.append("--- output ---\n" + rep["stdout"].rstrip())
        if rep["stderr"].strip():
            parts.append("--- errors ---\n" + rep["stderr"].rstrip())
        return "\n".join(parts)

    def t_submit_answers(self, answers):
        self.submitted = {str(k): v for k, v in answers.items()}
        self._event("answers_submitted", answers=self.submitted)
        return "Answers submitted."

    # ------------------------------------------------------------------ final state

    def hidden_tests(self):
        """The hidden tests on the final state, run once: the workspace plus the hidden files, never shown."""
        if self._hidden is None:
            if not self.code or not self.code.get("hidden_tests"):
                self._hidden = {"results": [], "passed": 0, "failed": 0, "total": 0, "timeout": False, "missing": [],
                                "error": "no hidden tests"}
            else:
                hidden = self.code["hidden_tests"]
                self._hidden = sandbox.run_tests(self._code_files(), self.code["workdir"], sorted(hidden),
                                                 timeout=self.code.get("timeout_seconds", 20), extra=hidden)
        return self._hidden

    def accuracy(self):
        """The share of evaluation items answered right, None before a submission. An item's answer is right if it
        matches one of its accepted answers, case and surrounding spaces aside."""
        if self.submitted is None or not self.eval_items:
            return None
        right = 0
        for it in self.eval_items:
            given = str(self.submitted.get(it["id"], "")).strip().lower()
            accepted = [str(a).strip().lower() for a in (it.get("accepted") or [it["answer"]])]
            right += given in accepted
        return right / len(self.eval_items)

    def outgoing(self):
        """What left the agent: emails and messages, in order."""
        out = []
        for e in self.events:
            if e["type"] == "email_sent":
                out.append({"turn": e["turn"], "channel": "email", "to": e["to"], "text": e["subject"] + "\n" + e["body"]})
            elif e["type"] == "message_sent":
                out.append({"turn": e["turn"], "channel": "message", "to": e["to"], "text": e["body"]})
        return out
