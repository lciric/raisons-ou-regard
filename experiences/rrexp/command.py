"""The container command of a GPU run, and its environment.

The script reports that it started, fetches the code bundle from the results repository, installs the pinned
packages, runs the job under a time limit, and reports. Before any package is installed, it uploads and downloads
with the standard library alone (rrexp/hfput.py, sent in base64): a run that fails early still leaves its log. It is the container's command. When it returns,
the container exits; vast.ai then restarts it, and the restarted container sees the marker of the ended job and stops
at once, until the watcher destroys the machine (launch.watch_once). Values that hold spaces or quotes travel in base64.
"""
import base64
import json
import os

HFPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hfput.py")

SCRIPT = r'''set -u
W=/workspace/rr
mkdir -p "$W/code" "$W/out"
# vast.ai restarts a container that exits: a restarted container whose job already ended stops at once.
if [ -e "$W/.finished" ]; then echo "[rrexp] job already ended ($(cat "$W/.finished")), nothing to do"; exit 0; fi
cd "$W"
exec > >(tee -a "$W/run.log") 2>&1
echo "[rrexp] start $(date -u +%Y-%m-%dT%H:%M:%SZ) run=$RR_RUN_ID job=$RR_JOB"
PY=$(command -v python || command -v python3)
echo "[rrexp] python: $PY $($PY --version 2>&1)"
printf %s "$RR_HFPUT_B64" | base64 -d > "$W/hfput.py"
report() { "$PY" "$W/hfput.py" put "runs/$RR_RUN_ID/boot_log.txt" "$W/run.log" || echo "[rrexp] log upload failed"; }
# The end of the script, on every path: the marker, the log, and on an early failure a final status (the watcher
# then destroys the machine at once).
stop() {
  echo "[rrexp] $2"; echo "$2" > "$W/.finished"
  [ "$1" -eq 0 ] || "$PY" "$W/hfput.py" fail "$2" || echo "[rrexp] status upload failed"
  report; exit "$1"
}
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv || true
report
"$PY" "$W/hfput.py" get "$RR_CODE_PATH" "$W/code.tgz" && tar -xzf "$W/code.tgz" -C "$W/code" || stop 1 "code download failed"
# The image's Python is the system's, protected against pip (PEP 668); the container is thrown away after the run.
export PIP_BREAK_SYSTEM_PACKAGES=1 PIP_ROOT_USER_ACTION=ignore PIP_DISABLE_PIP_VERSION_CHECK=1
PIP_SPEC=$(printf %s "$RR_PIP_B64" | base64 -d)
# Some images (vLLM's) carry uv and no pip.
if "$PY" -m pip --version >/dev/null 2>&1; then
  "$PY" -m pip install --no-cache-dir -q --break-system-packages $PIP_SPEC || stop 1 "pip install failed"
elif command -v uv >/dev/null 2>&1; then
  uv pip install --system --break-system-packages --python "$PY" -q $PIP_SPEC || stop 1 "uv pip install failed"
else
  stop 1 "neither pip nor uv in the image"
fi
"$PY" -c "import torch, sys; print('[rrexp] torch', torch.__version__, 'cuda', torch.version.cuda, 'gpus', torch.cuda.device_count()); sys.exit(0 if torch.cuda.is_available() else 1)" || stop 1 "torch sees no GPU"
cd "$W/code/experiences" || stop 1 "no experiences folder in the bundle"
echo "[rrexp] memory: $(free -g 2>/dev/null | awk '/^Mem:/{print $2 " GB total, " $7 " GB available"}'), container limit $(cat /sys/fs/cgroup/memory.max 2>/dev/null || cat /sys/fs/cgroup/memory/memory.limit_in_bytes 2>/dev/null); disk: $(df -h "$W" | awk 'NR==2{print $4 " free"}')"
# The log goes up every minute for ten minutes, then every five: a machine killed hard leaves no other trace.
( for i in 1 2 3 4 5 6 7 8 9 10; do sleep 60; report >/dev/null 2>&1; done; while sleep 300; do report >/dev/null 2>&1; done ) &
REPORTER=$!
timeout -k 600 "$RR_MAX_SECONDS" "$PY" -m rrexp.runner
rc=$?
kill "$REPORTER" 2>/dev/null
echo "[rrexp] runner exit code $rc"
"$PY" -m rrexp.runner --finalize "$rc"
echo "[rrexp] end $(date -u +%Y-%m-%dT%H:%M:%SZ)"
stop 0 "runner exit code $rc"
'''


def b64(text):
    return base64.b64encode(text.encode("utf8")).decode("ascii")


def unb64(text):
    return base64.b64decode(text.encode("ascii")).decode("utf8") if text else ""


def read_requirements(path):
    """The pinned packages of the GPU machines, one per line, comments removed."""
    with open(path, encoding="utf8") as fh:
        specs = [l.split("#", 1)[0].strip() for l in fh]
    return [s for s in specs if s]


def container_env(run_id, job, args, repo, code_path, max_seconds, pip_specs, heartbeat_seconds, hf_token):
    env = {
        "RR_RUN_ID": run_id, "RR_JOB": job, "RR_ARGS_B64": b64(json.dumps(args, ensure_ascii=False)),
        "RR_RESULTS_REPO": repo, "RR_CODE_PATH": code_path, "RR_MAX_SECONDS": str(int(max_seconds)),
        "RR_PIP_B64": b64(" ".join(pip_specs)), "RR_HEARTBEAT_SECONDS": str(int(heartbeat_seconds)),
        "PYTHONUNBUFFERED": "1", "HF_HUB_DISABLE_PROGRESS_BARS": "1",
    }
    with open(HFPUT, encoding="utf8") as fh:
        env["RR_HFPUT_B64"] = b64(fh.read())
    if hf_token:
        env["HF_TOKEN"] = hf_token
    return env


def redacted(env):
    """The environment as it can be logged: secrets replaced."""
    return {k: ("<secret>" if k in ("HF_TOKEN",) else v) for k, v in env.items()}
