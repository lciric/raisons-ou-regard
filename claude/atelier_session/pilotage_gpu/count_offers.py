"""How many H100 SXM offers pass the config's filters now (the launcher's own query)."""
from rrexp import launch as L
from rrexp.vast import Vast, offer_query
cfg = L.load_config()
gpu = [g for g in cfg["gpus"] if g["name"] == "H100 SXM"][0]
print(len(Vast().search_offers(offer_query(gpu, 1, cfg["disk_gb"], cfg["filters"], cfg["max_dph_per_gpu"]))))
