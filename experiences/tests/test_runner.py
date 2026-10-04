"""Offline tests of the GPU-side runner: statuses, outputs, failures, the time limit, the final status."""
import shutil
import sys
import tempfile
import types
import unittest
from pathlib import Path

from rrexp import runner


class RecordingHub:
    def __init__(self):
        self.json, self.files, self.folders = {}, {}, {}

    def put_json(self, path, obj, message=None):
        self.json[path] = dict(obj)

    def put_file(self, path, local, message=None):
        self.files[path] = Path(local).read_text(encoding="utf8")

    def put_folder(self, path, local, message=None, ignore=None):
        self.folders[path] = (sorted(str(p.relative_to(local)) for p in Path(local).rglob("*") if p.is_file()), ignore)

    def get_json(self, path):
        return self.json.get(path)


def _job(name, fn):
    mod = types.ModuleType(f"rrexp.jobs.{name}")
    mod.run = fn
    sys.modules[f"rrexp.jobs.{name}"] = mod


def ok_job(ctx):
    (ctx.out / "result.txt").write_text("42", encoding="utf8")
    big = ctx.out / "checkpoints"
    big.mkdir()
    (big / "adapter.bin").write_text("x", encoding="utf8")
    ctx.self_uploaded.append(str(big.resolve()))
    ctx.progress = "half way"
    return {"answer": 42}


def failing_job(ctx):
    raise ValueError("boom")


def slow_job(ctx):
    raise runner.TimeLimit("SIGTERM received")


def signalled_job(ctx):
    """A real SIGTERM in the middle of the work, as at a machine's time limit."""
    import os
    import signal
    import time
    (ctx.out / "adapter.bin").write_text("weights", encoding="utf8")
    os.kill(os.getpid(), signal.SIGTERM)
    time.sleep(5)
    return {"never": True}


class SignallingHub(RecordingHub):
    """A hub whose upload receives a second SIGTERM (timeout signals the process and then its group)."""

    def put_folder(self, path, local, message=None, ignore=None):
        import os
        import signal
        os.kill(os.getpid(), signal.SIGTERM)
        super().put_folder(path, local, message, ignore)


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.log = self.tmp / "run.log"
        self.log.write_text("log line\n", encoding="utf8")
        _job("essai_ok", ok_job)
        _job("essai_echec", failing_job)
        _job("essai_lent", slow_job)
        _job("essai_signal", signalled_job)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_done_run_uploads_outputs_but_not_self_uploaded(self):
        hub = RecordingHub()
        st = runner.run_job("r1", "essai_ok", {"a": 1}, hub, out_root=self.tmp / "out", log=self.log, heartbeat_seconds=3600)
        self.assertEqual(st["state"], "done")
        self.assertEqual(st["result"], {"answer": 42})
        self.assertEqual(hub.json["runs/r1/status.json"]["state"], "done")
        files, ignore = hub.folders["runs/r1/out"]
        self.assertIn("result.txt", files)
        self.assertEqual(ignore, ["checkpoints/**"])
        self.assertEqual(hub.files["runs/r1/log.txt"], "log line\n")

    def test_failure_is_reported(self):
        hub = RecordingHub()
        st = runner.run_job("r2", "essai_echec", {}, hub, out_root=self.tmp / "out", log=self.log, heartbeat_seconds=3600)
        self.assertEqual(st["state"], "failed")
        self.assertIn("ValueError: boom", st["error"])

    def test_time_limit_is_reported(self):
        hub = RecordingHub()
        st = runner.run_job("r3", "essai_lent", {}, hub, out_root=self.tmp / "out", log=self.log, heartbeat_seconds=3600)
        self.assertEqual(st["state"], "timeout")

    def test_a_real_signal_still_uploads_the_outputs(self):
        import signal
        before = signal.signal(signal.SIGTERM, runner._on_sigterm)
        try:
            hub = SignallingHub()
            st = runner.run_job("r6", "essai_signal", {}, hub, out_root=self.tmp / "out", log=self.log, heartbeat_seconds=3600)
            self.assertEqual(st["state"], "timeout")
            self.assertIn("adapter.bin", hub.folders["runs/r6/out"][0])      # the second signal did not cut the upload
            self.assertEqual(hub.json["runs/r6/status.json"]["state"], "timeout")
            self.assertIs(signal.getsignal(signal.SIGTERM), runner._on_sigterm)
        finally:
            signal.signal(signal.SIGTERM, before)

    def test_time_left(self):
        import os
        old = os.environ.pop("RR_MAX_SECONDS", None)
        try:
            self.assertIsNone(runner.JobContext("r", "j", {}, self.tmp, None).time_left())
            os.environ["RR_MAX_SECONDS"] = "100"
            left = runner.JobContext("r", "j", {}, self.tmp, None).time_left()
            self.assertTrue(99 < left <= 100)
        finally:
            os.environ.pop("RR_MAX_SECONDS", None)
            if old is not None:
                os.environ["RR_MAX_SECONDS"] = old

    def test_finalize_writes_a_final_status_once(self):
        hub = RecordingHub()
        hub.json["runs/r4/status.json"] = {"run_id": "r4", "state": "running"}
        st = runner.finalize("r4", "essai_ok", 124, hub, log=self.log)
        self.assertEqual(st["state"], "timeout")
        hub.json["runs/r5/status.json"] = {"run_id": "r5", "state": "done"}
        self.assertEqual(runner.finalize("r5", "essai_ok", 0, hub, log=self.log)["state"], "done")


if __name__ == "__main__":
    unittest.main()
