"""La simulation de puissance de la porte des raisons retrouve les vérités nettes."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import puissance_raisons as pw  # noqa: E402


class TestPuissance(unittest.TestCase):
    def test_counts_follow_the_rates(self):
        rng = np.random.default_rng(0)
        k, n = pw.simulate_counts(rng, pw.arms(0.4, 0.3, 0.2, 0.2, 0.1, 0.1), seeds=4, scenarios=500, gens=10, scen_sd=0.0)
        rates = k.sum(axis=(0, 1)) / n.sum(axis=(0, 1))
        self.assertTrue(np.allclose(rates, [0.4, 0.3, 0.2, 0.2, 0.1, 0.1], atol=0.01))

    def test_large_effects_are_found(self):
        cfg = {"deploiement": pw.arms(0.40, 0.30, 0.20, 0.20, 0.10, 0.10), "seeds": 8, "scenarios": 300, "gens": 5,
               "scen_sd": 0.03, "seed_sd": 0.0}
        self.assertGreaterEqual(pw.power(cfg, reps=5, n_boot=100).get("gain des raisons, avec un gain de lien", 0), 0.8)
        cfg = dict(cfg, deploiement=pw.arms(0.30, 0.30, 0.30, 0.30, 0.30, 0.30))
        self.assertGreaterEqual(pw.power(cfg, reps=5, n_boot=100).get("pas de gain", 0), 0.8)


if __name__ == "__main__":
    unittest.main()
