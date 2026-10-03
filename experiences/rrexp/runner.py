"""Runs one job on a GPU machine and reports through the results repository.

python -m rrexp.runner              runs the job named by RR_JOB, with status heartbeats
python -m rrexp.runner --finalize N  after the runner: writes a final status if it could not (time limit, crash)

A job is a module of rrexp.jobs with a function run(ctx) that returns a small JSON summary. Its files go in
ctx.out; the runner uploads them at the end, except what the job marks as uploaded by itself (large artifacts).
"""
import base64
import importlib
import json
import os
import platform
import signal
import socket
import subprocess
import sys
import threading
import time
import traceback
from pathlib import Path

from .hub import Hub

OUT_ROOT = Path(os.environ.get("RR_OUT_ROOT", "/workspace/rr/out"))
LOG = Path(os.environ.get("RR_LOG", "/workspace/rr/run.log"))
FINAL = ("done", "failed", "timeout")
PACKAGES = ("torch", "transformers", "peft", "accelerate", "huggingface_hub", "hf_xet", "safetensors", "tokenizers", "numpy")


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def machine_info():
    info = {"hostname": socket.gethostname(), "python": platform.python_version()}
    try:
        info["gpus"] = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
                                      capture_output=True, text=True, timeout=60).stdout.strip().splitlines()
    except Exception as e:  # noqa: BLE001
        info["gpus"] = f"nvidia-smi failed: {e}"
    import importlib.metadata as md
    info["packages"] = {}
    for p in PACKAGES:
        try:
            info["packages"][p] = md.version(p)
        except md.PackageNotFoundError:
            info["packages"][p] = None
    try:
        import torch  # noqa: WPS433
        info["cuda"] = torch.version.cuda
        info["cuda_available"] = torch.cuda.is_available()
    except Exception as e:  # noqa: BLE001
        info["cuda"] = f"torch unavailable: {e}"
    return info


class JobContext:
    """What a job sees: its run id, its arguments, its output folder, the results repository, a progress line."""

    def __init__(self, run_id, job, args, out, hub):
        self.run_id, self.job, self.args, self.out, self.hub = run_id, job, args, Path(out), hub
        self.progress = ""
        self.self_uploaded = []   # paths under out that the job uploaded itself; the runner skips them

    def run_path(self, rel):
        return f"runs/{self.run_id}/{rel}"

    def upload_file(self, local, rel):
        self.hub.put_file(self.run_path(rel), local)

    def upload_folder(self, local, rel):
        self.hub.put_folder(self.run_path(rel), local)
        self.self_uploaded.append(str(Path(local).resolve()))


class Heartbeat(threading.Thread):
    def __init__(self, hub, path, status, ctx, every):
        super().__init__(daemon=True)
        self.hub, self.path, self.status, self.ctx, self.every = hub, path, status, ctx, every
        self.halt = threading.Event()

    def run(self):
        while not self.halt.wait(self.every):
            self.status["heartbeat"] = now()
            self.status["progress"] = self.ctx.progress
            try:
                self.hub.put_json(self.path, self.status, "heartbeat")
            except Exception as e:  # noqa: BLE001  (a missed heartbeat must not stop the job)
                print(f"[rrexp] heartbeat failed: {type(e).__name__}", flush=True)

    def stop(self):
        self.halt.set()


class TimeLimit(Exception):
    pass


def _on_sigterm(signum, frame):
    raise TimeLimit("SIGTERM received: the run's time limit was reached")


def run_job(run_id, job, args, hub, out_root=OUT_ROOT, log=LOG, heartbeat_seconds=300):
    out = Path(out_root) / run_id
    out.mkdir(parents=True, exist_ok=True)
    spath = f"runs/{run_id}/status.json"
    status = {"run_id": run_id, "job": job, "state": "running", "started": now(), "heartbeat": now(),
              "machine": machine_info(), "args": args}
    hub.put_json(spath, status, "start")
    ctx = JobContext(run_id, job, args, out, hub)
    hb = Heartbeat(hub, spath, status, ctx, heartbeat_seconds)
    hb.start()
    try:
        mod = importlib.import_module(f"rrexp.jobs.{job}")
        status["result"] = mod.run(ctx)
        status["state"] = "done"
    except TimeLimit:
        status["state"] = "timeout"
        status["error"] = traceback.format_exc()[-4000:]
    except BaseException:  # noqa: BLE001  (everything is reported, then the run ends)
        status["state"] = "failed"
        status["error"] = traceback.format_exc()[-4000:]
    finally:
        hb.stop()
        status["ended"] = now()
        status["progress"] = ctx.progress
        base = str(out.resolve())
        skip = [os.path.relpath(p, base) + "/**" for p in ctx.self_uploaded if p.startswith(base)]
        try:
            if any(out.iterdir()):
                hub.put_folder(f"runs/{run_id}/out", out, "outputs", ignore=skip or None)
        except Exception as e:  # noqa: BLE001
            status.setdefault("upload_errors", []).append(f"outputs: {type(e).__name__}: {e}"[:500])
        try:
            if Path(log).exists():
                hub.put_file(f"runs/{run_id}/log.txt", log, "log")
        except Exception as e:  # noqa: BLE001
            status.setdefault("upload_errors", []).append(f"log: {type(e).__name__}"[:500])
        hub.put_json(spath, status, f"final: {status['state']}")
    return status


def finalize(run_id, job, rc, hub, log=LOG):
    """Writes a final status when the runner could not (killed at the time limit, crashed), and the full log."""
    spath = f"runs/{run_id}/status.json"
    st = hub.get_json(spath) or {"run_id": run_id, "job": job}
    if st.get("state") not in FINAL:
        st["state"] = "timeout" if rc in (124, 137) else "failed"
        st["exit_code"] = rc
        st["ended"] = now()
        hub.put_json(spath, st, f"final (finalize): {st['state']}")
    if Path(log).exists():
        hub.put_file(f"runs/{run_id}/log.txt", log, "log (final)")
    return st


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    run_id, job = os.environ["RR_RUN_ID"], os.environ["RR_JOB"]
    hub = Hub()
    if argv and argv[0] == "--finalize":
        st = finalize(run_id, job, int(argv[1]), hub)
        print(f"[rrexp] final state: {st.get('state')}", flush=True)
        return 0
    args = json.loads(base64.b64decode(os.environ.get("RR_ARGS_B64") or "e30=").decode("utf8"))
    signal.signal(signal.SIGTERM, _on_sigterm)
    st = run_job(run_id, job, args, hub, heartbeat_seconds=int(os.environ.get("RR_HEARTBEAT_SECONDS", "300")))
    print(f"[rrexp] state: {st['state']}", flush=True)
    return 0 if st["state"] == "done" else 1


if __name__ == "__main__":
    sys.exit(main())
