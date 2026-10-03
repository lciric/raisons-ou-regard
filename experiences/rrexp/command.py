"""The container command of a GPU run, and its environment.

The script reports that it started, fetches the code bundle from the results repository, installs the pinned
packages, runs the job under a time limit, and reports. Before any package is installed, it uploads and downloads
with the standard library alone (rrexp/hfput.py, sent in base64): a run that fails early still leaves its log. It is the container's command: when it returns, the container exits and the GPU is no
longer billed. Values that hold spaces or quotes travel in base64.
"""
import base64
import json
import os

HFPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hfput.py")

SCRIPT = r'''set -u
W=/workspace/rr
mkdir -p "$W/code" "$W/out"
cd "$W"
exec > >(tee -a "$W/run.log") 2>&1
echo "[rrexp] start $(date -u +%Y-%m-%dT%H:%M:%SZ) run=$RR_RUN_ID job=$RR_JOB"
PY=$(command -v python || command -v python3)
echo "[rrexp] python: $PY $($PY --version 2>&1)"
printf %s "$RR_HFPUT_B64" | base64 -d > "$W/hfput.py"
report() { "$PY" "$W/hfput.py" put "runs/$RR_RUN_ID/boot_log.txt" "$W/run.log" || echo "[rrexp] log upload failed"; }
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv || true
report
"$PY" "$W/hfput.py" get "$RR_CODE_PATH" "$W/code.tgz" && tar -xzf "$W/code.tgz" -C "$W/code" || { echo "[rrexp] code download failed"; report; exit 1; }
PIP_SPEC=$(printf %s "$RR_PIP_B64" | base64 -d)
"$PY" -m pip install --no-cache-dir -q $PIP_SPEC || { echo "[rrexp] pip install failed"; report; exit 1; }
cd "$W/code/experiences" || { report; exit 1; }
timeout -k 120 "$RR_MAX_SECONDS" "$PY" -m rrexp.runner
rc=$?
echo "[rrexp] runner exit code $rc"
"$PY" -m rrexp.runner --finalize "$rc"
echo "[rrexp] end $(date -u +%Y-%m-%dT%H:%M:%SZ)"
report
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
