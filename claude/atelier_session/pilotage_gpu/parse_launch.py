import json, sys
t = sys.stdin.read()
try:
    r = json.loads(t[t.index("{"):])
    o = r.get("offer", {})
    print(r["run_id"], r["state"], o.get("gpu_name"), round(o.get("dph_total") or 0, 3), "machine", o.get("machine_id"), "git", r["bundle"]["git_head"][:8])
except Exception as e:  # noqa: BLE001
    print("unparsed:", type(e).__name__)
