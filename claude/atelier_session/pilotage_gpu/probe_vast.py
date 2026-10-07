import json
from rrexp.vast import Vast
v = Vast()
u = v.user()
print("credit:", u.get("credit"), "balance:", u.get("balance"))
r = v._call("GET", "/instances/")
inst = r.get("instances", []) if isinstance(r, dict) else r
print("instances:", len(inst))
for i in inst:
    print(i.get("id"), i.get("label"), i.get("actual_status"), i.get("intended_status"), i.get("gpu_name"), i.get("dph_total"))
