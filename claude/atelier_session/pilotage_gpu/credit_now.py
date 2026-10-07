"""The vast.ai credit now, in dollars (the launcher's own check)."""
from rrexp import launch as L
print(round(float(L.check(L.load_config())["vast"]["credit_usd"]), 2))
