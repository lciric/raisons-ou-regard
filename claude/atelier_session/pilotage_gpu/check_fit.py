"""Waits until run B has fitted its erasure on the starting model, or failed; prints what it finds."""
import json, sys, time
from rrexp.hub import Hub
run = sys.argv[1]
hub, end = Hub(), time.time() + 45 * 60
while time.time() < end:
    st = hub.get_json(f"runs/{run}/status.json") or {}
    if st.get("state") in ("done", "failed", "timeout"):
        print("final state", st.get("state"), (st.get("error") or "")[-1500:])
        sys.exit(0)
    try:
        res = hub.get_json(f"runs/{run}/out/results.json") or {}
    except Exception:  # noqa: BLE001
        res = {}
    if res.get("erasure"):
        for k, v in res["erasure"].items():
            print("fitted", k, {x: v.get(x) for x in ("fit_on", "states", "directions_per_layer", "sets")})
        print("progress", st.get("progress"), "| gpu", (st.get("machine") or {}).get("gpus"))
        sys.exit(0)
    time.sleep(60)
print("no erasure after 45 min; progress:", (hub.get_json(f"runs/{run}/status.json") or {}).get("progress"))
