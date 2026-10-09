"""Les variantes des simulations de puissance : un niveau propre à chaque entraînement (règle du regard), et des écarts
corrélés entre bras au sein d'une graine (porte des raisons)."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import puissance_raisons_correlation as prc  # noqa: E402
import puissance_regard_entrainements as pre  # noqa: E402
from puissance_raisons import TRUTHS  # noqa: E402


class TestVariantes(unittest.TestCase):
    def test_a_run_level_is_shared_by_both_interventions(self):
        rng = np.random.default_rng(0)
        k, n = pre.simulate_counts(rng, 0.25, 10, 0.0, seeds=6, scenarios=400, gens=50, scen_sd=0.0, seed_sd_arm=0.08)
        rate = k.sum(axis=1) / n.sum(axis=1)                              # [graine, bras, intervention]
        corr = np.corrcoef(rate[:, :, 0].ravel(), rate[:, :, 1].ravel())[0, 1]
        self.assertGreater(corr, 0.95)                                    # f = 0 : l'inhibition ne change rien

    def test_correlated_runs_across_arms(self):
        for rho, lo, hi in ((0.0, -0.6, 0.6), (0.95, 0.85, 1.0)):
            rng = np.random.default_rng(1)
            k, n = prc.simulate_counts(rng, TRUTHS["aucun"], seeds=40, scenarios=200, gens=50, scen_sd=0.0, seed_sd=0.05, rho=rho)
            rate = k.sum(axis=1) / n.sum(axis=1)                          # [graine, bras]
            c = np.corrcoef(rate[:, 0], rate[:, 4])[0, 1]
            self.assertTrue(lo <= c <= hi, (rho, c))


if __name__ == "__main__":
    unittest.main()
