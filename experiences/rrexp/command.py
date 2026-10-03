"""The container command of a GPU run, and its environment.

The script installs the pinned packages, fetches the code bundle from the results repository, runs the job under a
time limit, and reports. It is the container's command: when it returns, the container exits and the GPU is no
longer billed. Values that hold spaces or quotes travel in base64.
"""
import base64
import json

SCRIPT = r'''set -u
W=/workspace/rr
mkdir -p "$W/code" "$W/out"
cd "$W"
exec > >(tee -a "$W/run.log") 2>&1
echo "[rrexp] start $(date -u +%Y-%m-%dT%H:%M:%SZ) run=$RR_RUN_ID job=$RR_JOB"
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv || true
PIP_SPEC=$(printf %s "$RR_PIP_B64" | base64 -d)
python -m pip install --no-cache-dir -q $PIP_SPEC || echo "[rrexp] pip install failed"
python - <<'PY' || echo "[rrexp] code download failed"
import os, tarfile
from huggingface_hub import hf_hub_download
p = hf_hub_download(os.environ["RR_RESULTS_REPO"], os.environ["RR_CODE_PATH"], repo_type="dataset", token=os.environ["HF_TOKEN"])
with tarfile.open(p) as t:
    t.extractall("/workspace/rr/code", filter="data")
PY
cd "$W/code/experiences" || exit 1
timeout -k 120 "$RR_MAX_SECONDS" python -m rrexp.runner
rc=$?
echo "[rrexp] runner exit code $rc"
python -m rrexp.runner --finalize "$rc"
echo "[rrexp] end $(date -u +%Y-%m-%dT%H:%M:%SZ)"
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
    if hf_token:
        env["HF_TOKEN"] = hf_token
    return env


def redacted(env):
    """The environment as it can be logged: secrets replaced."""
    return {k: ("<secret>" if k in ("HF_TOKEN",) else v) for k, v in env.items()}
