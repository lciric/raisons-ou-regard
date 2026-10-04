"""Offline tests of the launcher: the vast.ai requests, the code bundle, the container script, the watch decisions."""
import base64
import json
import os
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path

from rrexp import bundle, command, launch
from rrexp.vast import Vast, create_payload, offer_query, pick_offer

HERE = Path(__file__).resolve().parent.parent


class FakeResponse:
    def __init__(self, status, payload):
        self.status_code, self._payload = status, payload
        self.content = json.dumps(payload).encode()
        self.text = json.dumps(payload)

    def json(self):
        return self._payload


class FakeHTTP:
    """Records the requests and answers from a script of (status, payload)."""

    def __init__(self, answers):
        self.answers, self.calls = list(answers), []

    def request(self, method, url, json=None, params=None, headers=None, timeout=None):
        self.calls.append({"method": method, "url": url, "json": json, "params": params, "headers": headers})
        return FakeResponse(*self.answers.pop(0))


class TestVastRequests(unittest.TestCase):
    def test_offer_query(self):
        cfg = launch.load_config()
        q = offer_query({"name": "A100 SXM4", "min_gpu_ram_gb": 79}, 2, 120, cfg["filters"], 4.0)
        self.assertEqual(q["gpu_name"], {"eq": "A100 SXM4"})
        self.assertEqual(q["num_gpus"], {"eq": 2})
        self.assertEqual(q["gpu_ram"], {"gte": 79000.0})
        self.assertEqual(q["dph_total"], {"lte": 8.0})
        self.assertEqual(q["datacenter"], {"eq": True})
        self.assertEqual(q["order"], [["dph_total", "asc"]])
        self.assertEqual(q["type"], "on-demand")
        for k in ("verified", "external", "rentable", "rented"):
            self.assertIn(k, q)

    def test_payload_runs_the_script_as_the_container_command(self):
        p = create_payload("img", {"A": "1"}, 100, "rr-x", "echo hi")
        self.assertEqual(p["runtype"], "args")
        self.assertEqual(p["onstart"], "bash")
        self.assertEqual(p["args"], ["-c", "echo hi"])
        self.assertTrue(p["cancel_unavail"])

    def test_retry_then_create_and_key_never_in_body(self):
        http = FakeHTTP([(503, {}), (200, {"success": True, "new_contract": 4242})])
        v = Vast(key="k-secret", http=http, sleep=lambda s: None)
        self.assertEqual(v.create_instance(7, create_payload("img", {}, 10, "l", "x")), 4242)
        self.assertEqual(len(http.calls), 2)
        self.assertTrue(http.calls[-1]["url"].endswith("/api/v0/asks/7/"))
        self.assertEqual(http.calls[-1]["headers"]["Authorization"], "Bearer k-secret")
        self.assertNotIn("k-secret", json.dumps(http.calls[-1]["json"]))

    def test_pick_offer_falls_back_in_order(self):
        cfg = launch.load_config()
        http = FakeHTTP([(200, {"offers": []}), (200, {"offers": [{"id": 9, "dph_total": 1.2}]})])
        v = Vast(key="k", http=http, sleep=lambda s: None)
        gpu, offer, tried = pick_offer(v, cfg["gpus"], 1, 120, cfg["filters"], 4.0)
        self.assertEqual(gpu["name"], "A100 SXM4")
        self.assertEqual(offer["id"], 9)
        self.assertEqual([t["offers"] for t in tried], [0, 1])

    def test_without_key_the_proxy_credential_is_used(self):
        http = FakeHTTP([(200, {"credit": 12.5})])
        old = os.environ.pop("VAST_API_KEY", None)
        try:
            v = Vast(http=http, sleep=lambda s: None)
            self.assertTrue(v.via_proxy)
            self.assertEqual(v.user()["credit"], 12.5)
            self.assertNotIn("Authorization", http.calls[0]["headers"])
            v401 = Vast(http=FakeHTTP([(401, {})]), sleep=lambda s: None)
            with self.assertRaises(Exception) as cm:
                v401.user()
            self.assertIn("API credential", str(cm.exception))
        finally:
            if old is not None:
                os.environ["VAST_API_KEY"] = old

    def test_missing_instance_is_none(self):
        v = Vast(key="k", http=FakeHTTP([(404, {"error": "no"})]), sleep=lambda s: None)
        self.assertIsNone(v.show_instance(5))


class TestBundleAndScript(unittest.TestCase):
    def test_bundle_is_reproducible_and_holds_the_code(self):
        tmp = tempfile.mkdtemp()
        try:
            a = bundle.build(os.path.join(tmp, "a"), allow_dirty=True)
            b = bundle.build(os.path.join(tmp, "b"), allow_dirty=True)
            self.assertEqual(a["sha256"], b["sha256"])
            with tarfile.open(a["path"]) as t:
                names = t.getnames()
            self.assertIn("experiences/rrexp/runner.py", names)
            self.assertIn("donnees/rrdata/render.py", names)
            self.assertFalse(any("__pycache__" in n or "/sorties/" in n or "/registre/" in n for n in names))
        finally:
            shutil.rmtree(tmp)

    def test_script_is_valid_bash(self):
        r = subprocess.run(["bash", "-n", "-c", command.SCRIPT], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_restarted_container_stops_at_once(self):
        tmp = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(tmp, "w"))
            with open(os.path.join(tmp, "w", ".finished"), "w") as fh:
                fh.write("runner exit code 0\n")
            script = command.SCRIPT.replace("W=/workspace/rr", f"W={tmp}/w")
            r = subprocess.run(["bash", "-c", script], capture_output=True, text=True, env={"PATH": os.environ["PATH"]})
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("job already ended", r.stdout)
            self.assertFalse(os.path.exists(os.path.join(tmp, "w", "run.log")))
        finally:
            shutil.rmtree(tmp)

    def test_env_encodes_and_redacts(self):
        env = command.container_env("run-1", "smoke", {"a": "b c"}, "u/r", "code/x.tar.gz", 3600, ["x==1", "y==2"], 300, "hf_secret")
        self.assertEqual(json.loads(command.unb64(env["RR_ARGS_B64"])), {"a": "b c"})
        self.assertEqual(command.unb64(env["RR_PIP_B64"]), "x==1 y==2")
        self.assertEqual(command.redacted(env)["HF_TOKEN"], "<secret>")
        self.assertNotIn("hf_secret", json.dumps(command.redacted(env)))

    def test_requirements_are_pinned(self):
        specs = command.read_requirements(HERE / "requirements_gpu.txt")
        self.assertTrue(specs)
        self.assertTrue(all("==" in s for s in specs), specs)

    def test_dry_run_has_no_secret(self):
        os.environ["HF_TOKEN"] = "hf_should_not_appear"
        try:
            rec = launch.launch(launch.load_config(), "smoke", {"batch_sizes": [1]}, dry_run=True, allow_dirty=True)
        finally:
            del os.environ["HF_TOKEN"]
        self.assertEqual(rec["state"], "dry_run")
        self.assertNotIn("hf_should_not_appear", json.dumps(rec))
        self.assertEqual(rec["env"]["HF_TOKEN"], "<secret>")


class TestWatchDecisions(unittest.TestCase):
    W = {"stale_minutes": 30, "loading_minutes": 40, "exited_grace_minutes": 10}

    def rec(self, **kw):
        r = {"run_id": "smoke-x", "launched": "2026-10-03T10:00:00Z", "max_hours": 3, "state": "launched"}
        r.update(kw)
        return r

    def t(self, minutes):
        return launch.parse_iso("2026-10-03T10:00:00Z") + 60 * minutes

    def test_finished_run(self):
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "exited"}, {"state": "done"}, self.W, self.t(20))[0], "finish")

    def test_stuck_before_running(self):
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "loading"}, None, self.W, self.t(10))[0], "wait")
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "loading"}, None, self.W, self.t(41))[0], "destroy")

    def test_silent_run(self):
        st = {"state": "running", "heartbeat": "2026-10-03T10:05:00Z"}
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "running"}, st, self.W, self.t(20))[0], "wait")
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "running"}, st, self.W, self.t(40))[0], "warn")
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "running"}, st, self.W, self.t(70))[0], "destroy")

    def test_no_time_limit(self):
        # max_hours 0: a run that keeps its heartbeat is never stopped for its age; a silent one still is
        r = self.rec(max_hours=0)
        week = 7 * 24 * 60
        fresh = {"state": "running", "heartbeat": "2026-10-10T09:55:00Z"}
        self.assertEqual(launch.assess(r, {"actual_status": "running"}, fresh, self.W, self.t(week))[0], "wait")
        stale = {"state": "running", "heartbeat": "2026-10-10T08:00:00Z"}
        self.assertEqual(launch.assess(r, {"actual_status": "running"}, stale, self.W, self.t(week))[0], "destroy")
        self.assertIn('if [ "$RR_MAX_SECONDS" -gt 0 ]', command.SCRIPT)

    def test_exited_without_status(self):
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "exited"}, None, self.W, self.t(30))[0], "mark_dead")
        r = self.rec(state="dead", dead_seen="2026-10-03T10:30:00Z")
        self.assertEqual(launch.assess(r, {"actual_status": "exited"}, None, self.W, self.t(35))[0], "wait")
        self.assertEqual(launch.assess(r, {"actual_status": "exited"}, None, self.W, self.t(41))[0], "destroy")

    def test_lost_and_time_limit(self):
        self.assertEqual(launch.assess(self.rec(), None, None, self.W, self.t(5))[0], "lost")
        st = {"state": "running", "heartbeat": "2026-10-03T13:29:00Z"}
        self.assertEqual(launch.assess(self.rec(), {"actual_status": "running"}, st, self.W, self.t(211))[0], "destroy")


class FakeVast:
    def __init__(self, rows):
        self.rows, self.destroyed = rows, []

    def show_instance(self, i):
        return self.rows.get(i)

    def destroy_instance(self, i):
        self.destroyed.append(i)


class FakeHub:
    def __init__(self, statuses):
        self.statuses = statuses

    def get_json(self, path):
        return self.statuses.get(path)


class TestWatchOnce(unittest.TestCase):
    def test_finish_destroys_and_records_cost(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            rec = {"run_id": "smoke-a", "launched": "2026-10-03T10:00:00Z", "max_hours": 3, "state": "launched", "instance_id": 11,
                   "offer": {"dph_total": 2.0}}
            launch.save_record(rec, tmp)
            v = FakeVast({11: {"actual_status": "exited"}})
            h = FakeHub({"runs/smoke-a/status.json": {"state": "done", "result": {"ok": 1}}})
            lines = launch.watch_once({"watch": TestWatchDecisions.W}, v, h, registry=tmp, results=tmp / "res",
                                      now_ts=launch.parse_iso("2026-10-03T10:30:00Z"), fetch_outputs=False)
            self.assertEqual(lines, [("smoke-a", "finish", "done")])
            self.assertEqual(v.destroyed, [11])
            after = launch.load_records(tmp)[0]
            self.assertEqual(after["state"], "done")
            self.assertEqual(after["cost_usd_upper_bound"], 1.0)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
