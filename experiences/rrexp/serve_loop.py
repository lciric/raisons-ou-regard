"""The passes of a data pipeline run whose generator is an open model in serve mode (decision 42, 8 October 2026).

One rental answers every pass (the job open_generate with "serve": true). For each stage of the pipeline, in order:
1. the stage runs here (python -m rrdata <stage>, in donnees/): the judges are Claude, called from this session, and the
   generator's requests that the cache cannot answer are queued;
2. "offline-status" writes the requests still waiting; if there are none, the stage is done;
3. they go to runs/<run_id>/serve/queue_NNN.jsonl in the results repository; the job answers them into
   runs/<run_id>/out/answers_NNN.jsonl, then writes out/report_NNN.json;
4. "offline-import" puts the answers into the pipeline's cache, and the stage runs again (back to 1).

The stages that call no generator (plan, assemble, audit, report) run once. "other_family" is answered by the generator
of another family (--role generator_other): the job then switches models. At the end, runs/<run_id>/serve/stop ends the
job. A refusal is cached by the pipeline and never sent again: running a stage again replays none.

Run again after a stop, it takes up where it was: a queue sent and not yet answered is awaited, never sent twice. With
max_minutes, it pauses before a new pass once that time is spent, without ending the job: a session's background task
lasts two hours at most, and the next piece takes up.
"""
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

GENERATOR_FREE = ("plan", "assemble", "audit", "report")
STAGE_ARGS = {"assemble": ["--allow-unchecked"]}   # the pilot's gates on the held-out scenarios cannot be met yet


def rrdata(donnees, config, args, log):
    """One command of the data pipeline, in donnees/: the JSON of its last line ("<stage> {...}")."""
    cmd = [sys.executable, "-m", "rrdata", *args, "--config", config]
    t0 = time.time()
    r = subprocess.run(cmd, cwd=str(donnees), capture_output=True, text=True)
    with open(log, "a", encoding="utf8") as fh:
        fh.write(f"\n$ {' '.join(cmd[1:])}  ({time.time() - t0:.0f} s, exit {r.returncode})\n{r.stdout[-20000:]}{r.stderr[-5000:]}\n")
    if r.returncode != 0:
        raise RuntimeError(f"rrdata {' '.join(args)} failed (exit {r.returncode}): {r.stderr[-800:]}")
    lines = [l for l in r.stdout.splitlines() if l.strip() and not l.startswith("[")]
    return json.loads(lines[-1].split(" ", 1)[1])


def numbers(names, pattern):
    return sorted(int(m.group(1)) for m in (re.fullmatch(pattern, Path(n).name) for n in names) if m)


def retry(f, tries=5, wait=20.0, sleep=time.sleep):
    for i in range(tries):
        try:
            return f()
        except Exception:  # noqa: BLE001
            if i == tries - 1:
                raise
            sleep(wait * (i + 1))


class Driver:
    def __init__(self, hub, run_id, donnees, config, log, poll=20.0, wait_minutes=90, max_passes=15, sleep=time.sleep,
                 max_minutes=None, clock=time.time):
        self.hub, self.run_id, self.donnees, self.config, self.log = hub, run_id, Path(donnees), config, Path(log)
        self.max_minutes, self.clock = max_minutes, clock
        self.t0 = clock()
        self.poll, self.wait_s, self.max_passes, self.sleep = poll, wait_minutes * 60, max_passes, sleep
        self.serve, self.out = f"runs/{run_id}/serve", f"runs/{run_id}/out"
        self.tmp = Path(tempfile.mkdtemp(prefix="rr-serve-"))
        self.passes = []

    def say(self, line):
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        print(f"{stamp}  {line}", flush=True)
        with open(self.log, "a", encoding="utf8") as fh:
            fh.write(f"{stamp}  {line}\n")

    def cmd(self, *args):
        return rrdata(self.donnees, self.config, list(args), self.log)

    def last_sent(self):
        """The last queue sent, and whether it was answered."""
        sent = numbers(retry(lambda: self.hub.list(self.serve + "/")), r"queue_(\d{3})\.jsonl")
        answered = numbers(retry(lambda: self.hub.list(self.out + "/")), r"report_(\d{3})\.json")
        n = sent[-1] if sent else 0
        return n, (n == 0 or n in answered)

    def await_answers(self, n):
        """Waits for out/report_NNN.json, then fetches the answers. The job's end (or failure) without it stops all."""
        t0 = time.time()
        while not retry(lambda: self.hub.exists(f"{self.out}/report_{n:03d}.json")):
            status = retry(lambda: self.hub.get_json(f"runs/{self.run_id}/status.json")) or {}
            if status.get("state") in ("done", "failed", "timeout"):
                raise RuntimeError(f"the job ended ({status.get('state')}: {str(status.get('error'))[:300]}) before answering queue {n}")
            if time.time() - t0 > self.wait_s:
                raise RuntimeError(f"no answer to queue {n} after {self.wait_s / 60:.0f} min")
            self.sleep(self.poll)
        report = retry(lambda: self.hub.get_json(f"{self.out}/report_{n:03d}.json"))
        path = retry(lambda: self.hub.download(f"{self.out}/answers_{n:03d}.jsonl", self.tmp))
        return path, report

    def import_answers(self, n, role):
        path, report = self.await_answers(n)
        imp = self.cmd("offline-import", "--role", role, "--answers", str(path))
        rec = {"pass": n, "role": role, **{k: report.get(k) for k in ("model", "requests", "answers", "errors", "generate_seconds",
                                                                        "load_seconds", "stages")}, "import": imp}
        self.passes.append(rec)
        self.say(f"pass {n}: {json.dumps(rec, ensure_ascii=False)}")

    def run(self, stages):
        n, answered = self.last_sent()
        if not answered:      # a queue sent before a stop: await it, never send it again
            role = self.role_of_queue(n)
            self.say(f"taking up: queue {n} ({role}) was sent and is not answered yet")
            self.import_answers(n, role)
        results = {}
        for stage in stages:
            if self.spent():
                return self.pause(stage, results)
            if stage in GENERATOR_FREE:
                results[stage] = self.cmd(stage, *STAGE_ARGS.get(stage, []))
                self.say(f"{stage}: {json.dumps(results[stage], ensure_ascii=False)[:600]}")
                continue
            role = "generator_other" if stage == "other_family" else "generator"
            for k in range(self.max_passes + 1):
                if k and self.spent():
                    return self.pause(stage, results)
                results[stage] = self.cmd(stage)
                st = self.cmd("offline-status", "--role", role)
                self.say(f"{stage}, run {k + 1}: {json.dumps(results[stage], ensure_ascii=False)[:300]}; waiting {st['waiting']}")
                if st["waiting"] == 0:
                    break
                if k == self.max_passes:
                    raise RuntimeError(f"{stage}: still {st['waiting']} requests waiting after {self.max_passes} passes")
                n += 1
                waiting = Path(st["waiting_file"])
                waiting = waiting if waiting.is_absolute() else self.donnees / waiting
                retry(lambda n=n, w=waiting, st=st: self.hub.put_file(f"{self.serve}/queue_{n:03d}.jsonl", str(w),
                                                                      f"serve: queue {n} ({stage}, {st['waiting']} requests)", patience=900))
                self.import_answers(n, role)
        retry(lambda: self.hub.put_bytes(f"{self.serve}/stop", b"stop\n", "serve: stop"))
        self.say("stop sent")
        return {"stages": results, "passes": self.passes}

    def spent(self):
        return bool(self.max_minutes) and self.clock() - self.t0 > 60 * float(self.max_minutes)

    def pause(self, stage, results):
        self.say(f"paused before {stage}: {self.max_minutes} minutes spent; the next piece takes up")
        return {"paused": stage, "stages": results, "passes": self.passes}

    def role_of_queue(self, n):
        path = retry(lambda: self.hub.download(f"{self.serve}/queue_{n:03d}.jsonl", self.tmp))
        with open(path, encoding="utf8") as fh:
            return json.loads(fh.readline()).get("role") or "generator"
