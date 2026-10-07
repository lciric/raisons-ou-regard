from rrexp import launch as L
print(sum(1 for r in L.load_records() if r.get("state") in ("launched", "dead")))
