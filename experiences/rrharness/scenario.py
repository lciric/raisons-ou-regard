"""The format of a held-out scenario, its two variants, and the insertion of a framing cue at a known place.

A scenario file holds one scenario and its two variants (programme v1.5, part 3):
- "occasion": the task, with the opportunity to act wrongly that defines the family;
- "benigne": the same task with no such opportunity (the legitimate task), whose programmed success says whether an
  arm acts better because it is more aligned or because it acts less.

    {"format": "rrharness-0.1", "id": ..., "family": ..., "title": ..., "fixture": bool,
     "base": {fields}, "variants": {"occasion": {overrides}, "benigne": {overrides}}}

A variant is the base, deep-merged with its overrides (a null removes a key; a list replaces a list). The fields:
- system_prompt, turns: what the model sees before its first turn. turns starts with a user turn; an assistant turn of
  the prefix is a tool call that the harness executes, so that its result agrees with the state;
- tools: the tools offered (tools.TOOLS); environment: the state (env.Env); max_turns;
- truth: what the judge is told of the scenario (task, authorized, aligned, misaligned);
- misaligned_if: the predicates of the misaligned actions; success_if: those of the legitimate task (outcome.py);
- judge_questions: the typed questions for what the environment does not measure;
- known_cases: an aligned script and misaligned examples, replayed before any use (replay.py).

**The framing cue** (programme v1.5, part 3: the framing set, "blended into the held-out scenarios"). A scenario marks
the places where a cue can go with a line {{cue:<slot>}}, for the four slots of the framing set: system_prompt,
document_note, message_footer, banner. The harness inserts the cue text itself, so it knows its exact text and can
mask it in what the judge sees. Only a place the model is sure to see counts: the system prompt, a user turn of the
prefix, or a file or email that the prefix reads. A neutral rendering removes every marker.
"""
import copy
import json
import re
from dataclasses import dataclass, field

from . import tools as T
from .parse import parse_output

FORMAT = "rrharness-0.1"
FAMILIES = ("replacement", "underperformance", "exfiltration", "weak_grader", "sabotage")
VARIANTS = ("occasion", "benigne")
CUE_SLOTS = ("system_prompt", "document_note", "message_footer", "banner")
MARK_RE = re.compile(r"\{\{cue:([A-Za-z_]+)\}\}")
LINE_MARK_RE = re.compile(r"^[ \t]*\{\{cue:([A-Za-z_]+)\}\}[ \t]*$")
PREDICATE_KINDS = ("copied", "file_changed", "mode_changed", "outgoing_contains", "called", "file_contains",
                   "file_exists", "literal_lookup", "value_changed", "tests_pass", "submitted", "accuracy_at_least",
                   "all_of", "any_of", "not")
TRUTH_KEYS = ("task", "authorized", "aligned", "misaligned")


def deep_merge(base, over):
    out = copy.deepcopy(base)
    for k, v in (over or {}).items():
        if v is None:
            out.pop(k, None)
        elif isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def fill_marks(text, slot=None, cue=None):
    """Replaces the marker lines of slot by cue, and removes the other marker lines."""
    if not text or "{{cue:" not in text:
        return text
    lines = text.splitlines(keepends=True)
    out = []
    for line in lines:
        m = LINE_MARK_RE.match(line.rstrip("\r\n"))
        if not m:
            out.append(line)
            continue
        if cue is not None and m.group(1) == slot:
            end = "\n" if line.endswith("\n") else ""
            out.append(cue + end)
    return "".join(out)


@dataclass
class Rendered:
    system: str
    turns: list
    environment: dict
    cue_text: str = None
    cue_slot: str = None


@dataclass
class Scenario:
    id: str
    family: str
    variant: str
    pair_id: str
    title: str
    data: dict = field(repr=False)
    fixture: bool = False

    @property
    def uid(self):
        return f"{self.pair_id}/{self.variant}"

    @property
    def tools(self):
        return list(self.data.get("tools") or [])

    @property
    def max_turns(self):
        return int(self.data.get("max_turns", 15))

    @property
    def truth(self):
        return self.data.get("truth") or {}

    def prefix_calls(self):
        """The tool calls of the prefix's assistant turns (validated in validate())."""
        calls = []
        for t in self.data.get("turns") or []:
            if t.get("role") == "assistant":
                p = parse_output(t.get("content", ""), self.tools)
                if p["call"]:
                    calls.append(p["call"])
        return calls

    def _locations(self):
        """(where, text) for every text that may hold a marker; where tells whether the model surely sees it."""
        env = self.data.get("environment") or {}
        seen_files, seen_emails = set(), set()
        for c in self.prefix_calls():
            if c["name"] == "read_file":
                seen_files.add(_norm_path(c["arguments"].get("path", ""), env))
            if c["name"] == "read_email":
                seen_emails.add(str(c["arguments"].get("email_id", "")).strip())
        locs = [("system_prompt", True, self.data.get("system_prompt", ""))]
        for i, t in enumerate(self.data.get("turns") or []):
            locs.append((f"turn {i}", t.get("role") == "user", t.get("content", "")))
        for path, f in (env.get("files") or {}).items():
            text = f if isinstance(f, str) else (f or {}).get("content", "")
            locs.append((f"file {path}", _norm_path(path, env) in seen_files, text))
        for m in env.get("inbox") or []:
            locs.append((f"email {m.get('id')}", str(m.get("id")) in seen_emails, m.get("body", "")))
        return locs

    def cue_slots(self, visible_only=True):
        slots = set()
        for _, visible, text in self._locations():
            if visible or not visible_only:
                for line in (text or "").splitlines():
                    m = LINE_MARK_RE.match(line)
                    if m:
                        slots.add(m.group(1))
        return slots

    def render(self, cue=None):
        """The scenario with a cue ({"slot", "text"}) at its markers, or neutral (cue None)."""
        slot = cue["slot"] if cue else None
        text = cue["text"] if cue else None
        if cue is not None and slot not in self.cue_slots(visible_only=True):
            raise ValueError(f"{self.uid}: no visible place for a cue of slot {slot!r}")
        d = self.data
        env = copy.deepcopy(d.get("environment") or {})
        for path, f in list((env.get("files") or {}).items()):
            if isinstance(f, str):
                env["files"][path] = fill_marks(f, slot, text)
            else:
                f = dict(f)
                f["content"] = fill_marks(f.get("content", ""), slot, text)
                env["files"][path] = f
        for m in env.get("inbox") or []:
            m["body"] = fill_marks(m.get("body", ""), slot, text)
        turns = [dict(t, content=fill_marks(t.get("content", ""), slot, text)) for t in d.get("turns") or []]
        return Rendered(system=fill_marks(d.get("system_prompt", ""), slot, text).strip(), turns=turns, environment=env,
                        cue_text=text, cue_slot=slot)


def _norm_path(path, env):
    import posixpath  # noqa: WPS433
    path = (path or "").strip()
    home = env.get("home", "/home/agent")
    if path == "~" or path.startswith("~/"):
        path = home + path[1:]
    if not path.startswith("/"):
        path = posixpath.join(env.get("cwd", "/"), path)
    return posixpath.normpath(path)


def expand(doc):
    """The two variants of a scenario file, as Scenario objects."""
    out = []
    for name in VARIANTS:
        if name not in (doc.get("variants") or {}):
            continue
        data = deep_merge(doc.get("base") or {}, doc["variants"][name] or {})
        out.append(Scenario(id=f"{doc['id']}/{name}", family=doc["family"], variant=name, pair_id=doc["id"],
                            title=doc.get("title", ""), data=data, fixture=bool(doc.get("fixture"))))
    return out


def load(path):
    with open(path, encoding="utf8") as fh:
        return expand(json.load(fh))


def _check_predicate(p, where, problems, ids=None):
    if not isinstance(p, dict) or p.get("kind") not in PREDICATE_KINDS:
        problems.append(f"{where}: unknown predicate {p!r}"[:200])
        return
    k = p["kind"]
    need = {"copied": ["src_prefix"], "file_changed": [], "mode_changed": ["path_prefix"],
            "outgoing_contains": ["regex"], "called": ["tool"], "file_contains": ["path", "regex"],
            "file_exists": ["path"], "literal_lookup": ["path", "literals"], "value_changed": ["path", "regex"],
            "tests_pass": ["suite"], "submitted": [], "accuracy_at_least": ["value"], "all_of": ["items"],
            "any_of": ["items"], "not": ["item"]}[k]
    for f in need:
        if f not in p:
            problems.append(f"{where}: predicate {k} needs {f}")
    if k == "file_changed" and not (p.get("path") or p.get("path_prefix")):
        problems.append(f"{where}: predicate file_changed needs path or path_prefix")
    for rx_key in ("regex", "to_regex"):
        if rx_key in p:
            try:
                re.compile(p[rx_key])
            except re.error as e:
                problems.append(f"{where}: bad regex {p[rx_key]!r}: {e}")
    if k == "called":
        for a, rx in (p.get("args") or {}).items():
            try:
                re.compile(rx)
            except re.error as e:
                problems.append(f"{where}: bad regex for argument {a}: {e}")
    if k in ("all_of", "any_of"):
        for j, q in enumerate(p.get("items") or []):
            _check_predicate(q, f"{where}.items[{j}]", problems)
    if k == "not" and "item" in p:
        _check_predicate(p["item"], f"{where}.item", problems)
    if ids is not None:
        if not p.get("id"):
            problems.append(f"{where}: a top-level predicate needs an id")
        elif p["id"] in ids:
            problems.append(f"{where}: duplicate id {p['id']}")
        else:
            ids.add(p["id"])


def validate(scn):
    """The problems of a scenario variant (an empty list when it is usable)."""
    problems = []
    d = scn.data
    if scn.family not in FAMILIES:
        problems.append(f"unknown family {scn.family!r}")
    if scn.variant not in VARIANTS:
        problems.append(f"unknown variant {scn.variant!r}")
    offered = scn.tools
    if not offered:
        problems.append("no tools offered")
    for t in offered:
        if t not in T.TOOLS:
            problems.append(f"unknown tool {t!r}")
    if not (d.get("system_prompt") or "").strip():
        problems.append("empty system prompt")
    turns = d.get("turns") or []
    if not turns or turns[0].get("role") != "user":
        problems.append("the prefix must start with a user turn")
    for i, t in enumerate(turns):
        if t.get("role") not in ("user", "assistant"):
            problems.append(f"turn {i}: role {t.get('role')!r} (the prefix holds user turns and assistant tool calls; "
                            "the harness computes the tool results)")
        if t.get("role") == "assistant":
            p = parse_output(t.get("content", ""), offered)
            if not p["call"]:
                problems.append(f"turn {i}: the assistant turn of the prefix must be one tool call")
            else:
                err = T.check_arguments(p["call"]["name"], p["call"]["arguments"], offered)
                if err:
                    problems.append(f"turn {i}: {err}")
    if not 1 <= scn.max_turns <= 50:
        problems.append(f"max_turns {scn.max_turns} outside 1-50")
    truth = scn.truth
    for k in TRUTH_KEYS:
        if not truth.get(k):
            problems.append(f"truth.{k} is missing")
    # the markers: whole lines, known slots, at least one visible place
    for where, _, text in scn._locations():
        for line in (text or "").splitlines():
            for m in MARK_RE.finditer(line):
                if m.group(1) not in CUE_SLOTS:
                    problems.append(f"{where}: unknown cue slot {m.group(1)!r}")
                if not LINE_MARK_RE.match(line):
                    problems.append(f"{where}: a cue marker must stand alone on its line")
    if not scn.cue_slots(visible_only=True):
        problems.append("no cue marker in a place the model surely sees")
    ids = set()
    for j, p in enumerate(d.get("misaligned_if") or []):
        _check_predicate(p, f"misaligned_if[{j}]", problems, ids)
    for j, p in enumerate(d.get("success_if") or []):
        _check_predicate(p, f"success_if[{j}]", problems, set())
    if not d.get("success_if"):
        problems.append("success_if is empty: the legitimate task must be measured")
    if scn.variant == "occasion" and not (d.get("misaligned_if") or d.get("judge_questions")):
        problems.append("an occasion variant needs misaligned_if or judge_questions")
    for j, q in enumerate(d.get("judge_questions") or []):
        for f in ("id", "applies_to", "question", "options", "misaligned_if"):
            if f not in q:
                problems.append(f"judge_questions[{j}] needs {f}")
        opts = q.get("options") or []
        if not 2 <= len(opts) <= 16:
            problems.append(f"judge_questions[{j}]: 2 to 16 options")
        for o in (q.get("misaligned_if") or []) + (q.get("invalid_if") or []):
            if o not in opts:
                problems.append(f"judge_questions[{j}]: {o!r} is not an option")
        for a in q.get("applies_to") or []:
            if a not in offered and a not in ("final_answer", "*"):
                problems.append(f"judge_questions[{j}]: applies to {a!r}, which is not offered")
        if q.get("id") in ids:
            problems.append(f"judge_questions[{j}]: id {q.get('id')} already used")
        ids.add(q.get("id"))
    env = d.get("environment") or {}
    code = env.get("code")
    if code:
        if not code.get("workdir"):
            problems.append("environment.code needs a workdir")
        for t in code.get("tests") or []:
            full = _norm_path(code["workdir"].rstrip("/") + "/" + t, env)
            if full not in {_norm_path(p, env) for p in env.get("files") or {}}:
                problems.append(f"visible test {t} is not among the files")
    if "run_tests" in offered and not (code and code.get("tests")):
        problems.append("run_tests is offered but the project has no tests")
    if "submit_answers" in offered and not env.get("eval_items"):
        problems.append("submit_answers is offered but there are no evaluation items")
    return problems
