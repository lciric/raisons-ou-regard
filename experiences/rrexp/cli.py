"""Command line, from the experiences/ folder: python -m rrexp <command>.

check                       keys present (yes or no), hosts reachable, token rights, vast.ai credit
launch <job> [--arg k=v]    rents a machine and starts a job (smoke, train_lora)
watch [--once]              follows the open runs, destroys the finished or stuck machines, fetches the outputs
list                        the runs of the registry
destroy <run_id>            destroys a run's machine by hand
send-data <name> <run_dir>  sends the arms of a pipeline run to data/<name>/ in the results repository
"""
import argparse
import json
import sys
import time

from . import launch as L


def _args(pairs):
    out = {}
    for kv in pairs:
        k, v = kv.split("=", 1)
        try:
            out[k] = json.loads(v)
        except json.JSONDecodeError:
            out[k] = v
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(prog="rrexp", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", default=None)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    pl = sub.add_parser("launch")
    pl.add_argument("job", choices=L.JOBS)
    pl.add_argument("--arg", action="append", default=[], help="job argument, key=value (value read as JSON when it can be)")
    pl.add_argument("--gpus", type=int, default=1, help="number of GPUs on the machine")
    pl.add_argument("--max-hours", type=float, default=None)
    pl.add_argument("--allow-dirty", action="store_true", help="bundle uncommitted changes (dry runs only)")
    pl.add_argument("--dry-run", action="store_true", help="build the bundle and the request, rent nothing")
    pl.add_argument("--no-hf-token", action="store_true", help="do not pass HF_TOKEN: the vast.ai account provides it")
    pw = sub.add_parser("watch")
    pw.add_argument("--once", action="store_true")
    sub.add_parser("list")
    pd = sub.add_parser("destroy")
    pd.add_argument("run_id")
    ps = sub.add_parser("send-data")
    ps.add_argument("name")
    ps.add_argument("run_dir", help="the pipeline's output folder, for instance ../donnees/sorties/pilote")
    a = ap.parse_args(argv)
    cfg = L.load_config(a.config)

    if a.command == "check":
        print(json.dumps(L.check(cfg), ensure_ascii=False, indent=1))
        return 0
    if a.command == "launch":
        rec = L.launch(cfg, a.job, _args(a.arg), num_gpus=a.gpus, max_hours=a.max_hours, allow_dirty=a.allow_dirty,
                       dry_run=a.dry_run, pass_hf_token=not a.no_hf_token)
        print(json.dumps(rec, ensure_ascii=False, indent=1))
        return 0
    if a.command == "list":
        for r in L.load_records():
            print(f"{r['run_id']}  {r.get('state'):9}  {r.get('offer', {}).get('gpu_name', '-'):10}  "
                  f"{r.get('offer', {}).get('dph_total', '-')} $/h  cost<= {r.get('cost_usd_upper_bound', '-')}  {r.get('reason', '')}")
        return 0
    from .hub import Hub
    hub = Hub()
    if a.command == "send-data":
        print(json.dumps(L.send_data(hub, a.name, a.run_dir), ensure_ascii=False, indent=1))
        return 0
    from .vast import Vast
    vast = Vast()
    if a.command == "destroy":
        print(json.dumps(L.destroy(vast, a.run_id), ensure_ascii=False, indent=1))
        return 0
    if a.command == "watch":
        while True:
            lines = L.watch_once(cfg, vast, hub)
            for run_id, action, reason in lines:
                print(f"{L.now_iso()}  {run_id}  {action}  {reason}", flush=True)
            open_runs = [r for r in L.load_records() if r.get("state") in ("launched", "dead")]
            if a.once or not open_runs:
                return 0
            time.sleep(cfg["watch"]["poll_seconds"])
    return 1


if __name__ == "__main__":
    sys.exit(main())
