"""Launching, watching and stopping GPU runs on vast.ai, from the session that holds the keys.

Every run has a record in experiences/registre/<run_id>.json, committed: the history of what ran, on which machine,
for how long, at which price. A copy goes to the results repository (runs/<run_id>/launch.json). Neither holds a
secret.
"""
import calendar
import hashlib
import json
import os
import secrets
import tempfile
import time
from pathlib import Path

import yaml

from . import bundle as bundle_mod
from .command import SCRIPT, container_env, read_requirements, redacted
from .vast import DEAD_STATUSES, create_payload, pick_offer

HERE = Path(__file__).resolve().parent.parent   # the experiences/ folder
REGISTRY = HERE / "registre"
RESULTS = HERE / "resultats"
JOBS = ("smoke", "train_lora", "extract_eval", "inhibition_degradation", "judge_jev", "sdf_documents", "organism",
        "organism_inhibition", "composite_check")
FINAL = ("done", "failed", "timeout")
OFFER_FIELDS = ("id", "machine_id", "host_id", "gpu_name", "num_gpus", "gpu_ram", "dph_total", "reliability", "geolocation",
                "datacenter", "cuda_max_good", "inet_down", "disk_space", "cpu_ram")


def load_config(path=None):
    with open(path or HERE / "config_calcul.yaml", encoding="utf8") as fh:
        return yaml.safe_load(fh)


def now_iso(ts=None):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts if ts is not None else time.time()))


def parse_iso(s):
    return calendar.timegm(time.strptime(s, "%Y-%m-%dT%H:%M:%SZ"))


def new_run_id(job, ts=None):
    return f"{job}-{time.strftime('%Y%m%d-%H%M%S', time.gmtime(ts if ts is not None else time.time()))}-{secrets.token_hex(2)}"


def save_record(rec, registry=REGISTRY):
    registry.mkdir(parents=True, exist_ok=True)
    with open(registry / f"{rec['run_id']}.json", "w", encoding="utf8") as fh:
        json.dump(rec, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")


def load_records(registry=REGISTRY):
    if not registry.exists():
        return []
    out = []
    for p in sorted(registry.glob("*.json")):
        with open(p, encoding="utf8") as fh:
            out.append(json.load(fh))
    return out


# ---------------------------------------------------------------- launch

def job_config(cfg, job):
    """The configuration for one job: cfg with the job's overrides (job_overrides.<job>: image, filters...) applied."""
    over = (cfg.get("job_overrides") or {}).get(job)
    if not over:
        return cfg
    out = dict(cfg)
    for k, v in over.items():
        out[k] = dict(cfg.get(k) or {}, **v) if isinstance(v, dict) and isinstance(cfg.get(k), dict) else v
    return out


def gpu_pool(gpus, names=None):
    """The GPU types to rent from, in the config's order: all of them, or only the named ones. A procedure that pools
    the comparator's draws asks for one card only (decision 33: draws are pooled only between runs on the same card)."""
    if not names:
        return list(gpus)
    known = [g["name"] for g in gpus]
    unknown = [n for n in names if n not in known]
    if unknown:
        raise ValueError(f"GPU types not in the config: {unknown}; known: {known}")
    return [g for g in gpus if g["name"] in names]


def launch(cfg, job, args, num_gpus=1, max_hours=None, gpus=None, allow_dirty=False, dry_run=False,
           vast=None, hub=None, pass_hf_token=True, registry=REGISTRY, gpu_names=None):
    """Builds the code bundle, sends it, rents the cheapest fitting machine, starts the job. Returns the record.
    gpu_names: only these GPU types of the config (gpu_pool)."""
    if job not in JOBS:
        raise ValueError(f"unknown job {job!r}; jobs: {', '.join(JOBS)}")
    # 0 means no time limit: the machine runs the job to its end, and the watcher still destroys a silent one
    max_hours = float(cfg["max_hours_default"] if max_hours is None else max_hours)
    cfg = job_config(cfg, job)
    pool = gpu_pool(gpus or cfg["gpus"], gpu_names)
    pip_specs = read_requirements(HERE / cfg["requirements"])
    extra = (cfg.get("job_requirements") or {}).get(job)
    if extra:   # a job that needs more installs it on its own machine only
        pip_specs = pip_specs + read_requirements(HERE / extra)
    b = bundle_mod.build(tempfile.mkdtemp(prefix="rrexp-bundle-"), allow_dirty=allow_dirty)
    run_id = new_run_id(job)
    rec = {"run_id": run_id, "job": job, "args": args, "created": now_iso(), "image": cfg["image"], "disk_gb": cfg["disk_gb"],
           "num_gpus": int(num_gpus), "max_hours": max_hours, "state": "launching", "script_sha256": hashlib.sha256(SCRIPT.encode()).hexdigest(),
           "bundle": {k: b[k] for k in ("sha256", "repo_path", "git_head", "dirty", "files", "bytes")}, "requirements": pip_specs}
    if dry_run:
        env = container_env(run_id, job, args, "<results repo>", b["repo_path"], max_hours * 3600, pip_specs, cfg["heartbeat_seconds"],
                            "<secret>" if pass_hf_token else None)
        rec.update(state="dry_run", env=redacted(env))
        return rec
    if hub is None:
        from .hub import Hub  # noqa: WPS433
        hub = Hub()
    if vast is None:
        from .vast import Vast  # noqa: WPS433
        vast = Vast()
    if not hub.exists(b["repo_path"]):
        hub.put_file(b["repo_path"], b["path"], f"code bundle {b['sha256'][:16]} (git {b['git_head'][:8]})")
    gpu, offer, tried = pick_offer(vast, pool, num_gpus, cfg["disk_gb"], cfg["filters"], cfg["max_dph_per_gpu"])
    rec["offers_tried"] = tried
    if offer is None:
        rec["state"] = "no_offer"
        save_record(rec, registry)
        raise RuntimeError(f"no offer matches: {tried}")
    rec["offer"] = {k: offer.get(k) for k in OFFER_FIELDS}
    env = container_env(run_id, job, args, hub.repo, b["repo_path"], max_hours * 3600, pip_specs, cfg["heartbeat_seconds"],
                        hub.token if pass_hf_token else None)
    rec["env"] = redacted(env)
    instance_id = vast.create_instance(offer["id"], create_payload(cfg["image"], env, cfg["disk_gb"], f"rr-{run_id}", SCRIPT))
    rec.update(instance_id=instance_id, state="launched", launched=now_iso())
    save_record(rec, registry)
    hub.put_json(f"runs/{run_id}/launch.json", rec, f"launch {run_id}")
    return rec


# ---------------------------------------------------------------- watch

def assess(rec, inst, status, wcfg, now_ts):
    """What to do with a launched run, from its record, its instance row and its status. Returns (action, reason).

    Actions: "finish" (final status written), "destroy" (stuck, silent or over time), "lost" (instance gone, no
    final status), "warn" (late heartbeat), "wait".
    """
    if status and status.get("state") in FINAL:
        return "finish", status["state"]
    if inst is None:
        return "lost", "the instance no longer exists and the run wrote no final status"
    launched = parse_iso(rec["launched"])
    age_min = (now_ts - launched) / 60
    actual = inst.get("actual_status")
    if actual in DEAD_STATUSES:
        seen = rec.get("dead_seen")
        if seen is None:
            return "mark_dead", f"container {actual}"
        if (now_ts - parse_iso(seen)) / 60 >= wcfg["exited_grace_minutes"]:
            return "destroy", f"container {actual} without a final status"
        return "wait", f"container {actual}; waiting for a final status"
    if actual != "running" and not status:
        if age_min >= wcfg["loading_minutes"]:
            return "destroy", f"still {actual or 'provisioning'} after {age_min:.0f} min"
        return "wait", f"{actual or 'provisioning'}"
    if status and status.get("state") == "running":
        hb_min = (now_ts - parse_iso(status["heartbeat"])) / 60
        if hb_min >= 2 * wcfg["stale_minutes"]:
            return "destroy", f"no heartbeat for {hb_min:.0f} min"
        if rec["max_hours"] and age_min >= rec["max_hours"] * 60 + 30:
            return "destroy", f"running {age_min:.0f} min, past the time limit"
        if hb_min >= wcfg["stale_minutes"]:
            return "warn", f"heartbeat {hb_min:.0f} min old"
        return "wait", status.get("progress") or "running"
    if rec["max_hours"] and age_min >= rec["max_hours"] * 60 + 30:
        return "destroy", f"{age_min:.0f} min, past the time limit"
    return "wait", actual or ""


def cost_estimate(rec, end_ts):
    """GPU price times the time since launch: an upper bound (billing starts at "running"; disk is extra)."""
    dph = (rec.get("offer") or {}).get("dph_total")
    if not dph or not rec.get("launched"):
        return None
    return round(dph * (end_ts - parse_iso(rec["launched"])) / 3600, 3)


def fetch(hub, run_id, dest=RESULTS):
    """The small outputs of a run (status, log, outputs; not the checkpoints) into experiences/resultats/<run_id>/."""
    target = dest / run_id
    target.mkdir(parents=True, exist_ok=True)
    hub.snapshot([f"runs/{run_id}/*", f"runs/{run_id}/out/**"], target, ignore=[f"runs/{run_id}/out/checkpoints/**", "*.safetensors", "*.bin", "*.pt"])
    return target


def _save_vast_log(vast, rec, results):
    """The container's last lines, from vast.ai, kept before the machine is destroyed. Returns a short note."""
    try:
        url = vast.request_logs(rec["instance_id"])
        if not url:
            return "no log URL"
        import requests  # noqa: WPS433
        for _ in range(10):
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                target = results / rec["run_id"]
                target.mkdir(parents=True, exist_ok=True)
                (target / "vast_log.txt").write_text(r.text, encoding="utf8")
                return f"saved ({len(r.text)} characters)"
            time.sleep(2)
        return f"log URL answered {r.status_code}"
    except Exception as e:  # noqa: BLE001
        return f"unavailable: {type(e).__name__}: {str(e)[:150]}"


def watch_once(cfg, vast, hub, registry=REGISTRY, results=RESULTS, now_ts=None, fetch_outputs=True):
    """One pass over the open runs. Returns one line per run: (run_id, action, reason)."""
    now_ts = now_ts if now_ts is not None else time.time()
    lines = []
    for rec in load_records(registry):
        if rec.get("state") not in ("launched", "dead"):
            continue
        inst = vast.show_instance(rec["instance_id"])
        status = hub.get_json(f"runs/{rec['run_id']}/status.json")
        action, reason = assess(rec, inst, status, cfg["watch"], now_ts)
        if action == "mark_dead":
            rec.update(state="dead", dead_seen=now_iso(now_ts))
        elif action in ("finish", "destroy", "lost"):
            if inst is not None:
                if action != "finish":
                    rec["vast_log"] = _save_vast_log(vast, rec, results)
                vast.destroy_instance(rec["instance_id"])
            rec["destroyed"] = now_iso(now_ts)
            rec["state"] = status["state"] if action == "finish" else ("lost" if action == "lost" else "killed")
            rec["reason"] = reason
            rec["cost_usd_upper_bound"] = cost_estimate(rec, now_ts)
            if status:
                rec["result"] = status.get("result")
                rec["error"] = status.get("error")
            if fetch_outputs:
                try:
                    rec["results_dir"] = str(fetch(hub, rec["run_id"], results).relative_to(HERE))
                except Exception as e:  # noqa: BLE001
                    rec["fetch_error"] = f"{type(e).__name__}: {e}"[:300]
        save_record(rec, registry)
        lines.append((rec["run_id"], action, reason))
    return lines


def destroy(vast, run_id, registry=REGISTRY, reason="destroyed by hand"):
    rec = next((r for r in load_records(registry) if r["run_id"] == run_id), None)
    if rec is None:
        raise KeyError(run_id)
    if rec.get("instance_id"):
        vast.destroy_instance(rec["instance_id"])
    rec.update(state="killed", reason=reason, destroyed=now_iso(), cost_usd_upper_bound=cost_estimate(rec, time.time()))
    save_record(rec, registry)
    return rec


# ---------------------------------------------------------------- data

DATA_FILES = ("final_items.jsonl", "gates.json", "manifest.json", "RAPPORT.md")


def send_data(hub, name, run_dir):
    """Sends the arms of a pipeline run (donnees/sorties/<run>/) to data/<name>/ in the results repository.

    The training reads them there. Returns the SHA-256 of each file sent, for the run's record.
    """
    run_dir = Path(run_dir)
    files = sorted((run_dir / "arms").glob("*.jsonl")) + [run_dir / f for f in DATA_FILES if (run_dir / f).exists()]
    if not (run_dir / "arms").exists() or not files:
        raise FileNotFoundError(f"no arms in {run_dir}: run the pipeline's assembly first")
    sums = {}
    for f in files:
        rel = f.relative_to(run_dir).as_posix()
        with open(f, "rb") as fh:
            sums[rel] = hashlib.sha256(fh.read()).hexdigest()
        hub.put_file(f"data/{name}/{rel}", f, f"data {name}: {rel}")
    hub.put_json(f"data/{name}/sha256.json", sums, f"data {name}: checksums")
    return sums


def send_cues(hub, name, run_dir):
    """Sends the cue sets of a pipeline run (donnees/sorties/indices/cues/) to data/<name>/cues/ in the results repository."""
    cdir = Path(run_dir) / "cues"
    files = sorted(cdir.glob("*.jsonl")) + [cdir / f for f in ("deployment_prompt.txt", "report.json") if (cdir / f).exists()]
    files = [f for f in files if not f.name.endswith("_batches.jsonl")]
    if not files:
        raise FileNotFoundError(f"no cue sets in {cdir}: run the pipeline's cues stage first")
    sums = {}
    for f in files:
        with open(f, "rb") as fh:
            sums[f.name] = hashlib.sha256(fh.read()).hexdigest()
        hub.put_file(f"data/{name}/cues/{f.name}", f, f"cues {name}: {f.name}")
    hub.put_json(f"data/{name}/cues/sha256.json", sums, f"cues {name}: checksums")
    return sums


# ---------------------------------------------------------------- check

def check(cfg, http_get=None):
    """Whether the session can launch: keys present (yes or no, never the value), hosts reachable, token rights, credit."""
    import requests  # noqa: WPS433
    http_get = http_get or (lambda url: requests.get(url, timeout=20))
    out = {"keys": {k: bool(os.environ.get(k)) for k in ("HF_TOKEN", "VAST_API_KEY", "RR_ANTHROPIC_API_KEY", "RR_RESULTS_REPO")},
           "ANTHROPIC_API_KEY_absent": not os.environ.get("ANTHROPIC_API_KEY")}
    out["network"] = {}
    for host, url in (("huggingface.co", "https://huggingface.co/api/whoami-v2"), ("console.vast.ai", "https://console.vast.ai/api/v0/"),
                      ("api.anthropic.com", "https://api.anthropic.com/")):
        try:
            r = http_get(url)
            out["network"][host] = f"reachable (HTTP {r.status_code})"
        except Exception as e:  # noqa: BLE001
            out["network"][host] = f"unreachable ({type(e).__name__})"
    if out["keys"]["HF_TOKEN"] and out["keys"]["RR_RESULTS_REPO"]:
        try:
            from .hub import Hub  # noqa: WPS433
            out["hugging_face"] = Hub().check(cfg.get("gated_model"))
        except Exception as e:  # noqa: BLE001
            out["hugging_face"] = f"error: {type(e).__name__}: {str(e)[:200]}"
    try:  # with VAST_API_KEY, or through the environment's API credential for console.vast.ai
        from .vast import Vast  # noqa: WPS433
        v = Vast()
        u = v.user()
        out["vast"] = {"credit_usd": u.get("credit"), "balance_usd": u.get("balance"),
                       "key": "VAST_API_KEY" if not v.via_proxy else "API credential of the environment"}
    except Exception as e:  # noqa: BLE001
        out["vast"] = f"error: {type(e).__name__}: {str(e)[:200]}"
    return out
