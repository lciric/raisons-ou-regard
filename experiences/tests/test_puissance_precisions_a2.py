"""La simulation des deux précisions : les cadrages appariés partagent les scénarios et les entraînements, et un gain
net sous évaluation seulement reste lu avec la première précision."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import precisions_a2 as pa  # noqa: E402
import puissance_precisions_a2 as pp  # noqa: E402
from puissance_raisons import TRUTHS  # noqa: E402


class TestSimulation(unittest.TestCase):
    def test_paired_framings_share_scenarios_and_runs(self):
        rates = TRUTHS["aucun"]
        corr = {}
        for paired in (False, True):
            k, n = pp.simulate_framings(np.random.default_rng(1), rates, rates, seeds=6, scenarios=300, gens=50,
                                        scen_sd=0.08, seed_sd=0.05, paired=paired)
            per_run = (k / n).mean(axis=2)                                   # [cadrage, graine, bras]
            corr[paired] = np.corrcoef(per_run[0].ravel(), per_run[1].ravel())[0, 1]
        self.assertGreater(corr[True], 0.9)
        self.assertLess(abs(corr[False]), 0.5)

    def test_a_clear_gain_under_evaluation_only_is_kept(self):
        cfg = {"case": "regard", "deploiement": TRUTHS["aucun"], "evaluation": TRUTHS["lien"], "seeds": 8,
               "scenarios": 300, "gens": 5, "scen_sd": 0.03, "seed_sd": 0.0, "paired": True}
        raw, new = pp.power(cfg, reps=5, n_boot=100)
        self.assertGreaterEqual(raw.get(pa.EVAL_SEULEMENT, 0), 0.8)
        self.assertGreaterEqual(new.get(pa.EVAL_SEULEMENT, 0), 0.8)


if __name__ == "__main__":
    unittest.main()
