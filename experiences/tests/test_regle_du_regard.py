"""La règle du test du regard, sur des épisodes simulés dont on connaît la vérité (programme v1.5, parties 6 et 7)."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import regle_du_regard as rr  # noqa: E402


def simulate(rates, seeds=10, scenarios=200, gens=6, seed_sd=0.0, rng_seed=0, invalid=0.0, seed_sd_inh=0.0):
    """Des épisodes : rates[(bras, intervention)] est le taux d'action désalignée ; seed_sd, l'écart-type, en taux, d'un
    effet de l'entraînement sur l'avantage (les graines sont partagées entre bras) ; seed_sd_inh, celui d'un effet de
    l'entraînement sur le bras raisons sous inhibition seulement (une dépendance au regard qui varie d'un entraînement
    à l'autre) ; chaque scénario a sa difficulté."""
    rng = np.random.default_rng(rng_seed)
    eps = []
    scen_eff = rng.normal(0, 0.05, scenarios)
    for s in range(seeds):
        seed_eff = rng.normal(0, seed_sd)
        seed_inh = rng.normal(0, seed_sd_inh)
        for c in range(scenarios):
            for (arm, iv), p in rates.items():
                q = p + scen_eff[c] + (seed_eff if arm == rr.RAISONS else 0.0)
                q += seed_inh if (arm == rr.RAISONS and iv == rr.INHIBITION) else 0.0
                q = min(max(q, 0.01), 0.99)
                for _ in range(gens):
                    u = rng.random()
                    out = "desaligne" if u < q else ("invalide" if u < q + invalid else "aligne")
                    eps.append({"arm": arm, "seed": s, "intervention": iv, "framing": "deploiement", "slot": "libre",
                                "family": "f", "scenario": c, "outcome": out})
    return eps


def rates(a_inh, r_inh, a_k, r_k):
    return {(rr.ACTIONS, rr.INHIBITION): a_inh, (rr.RAISONS, rr.INHIBITION): r_inh,
            (rr.ACTIONS, rr.COMPARATEUR): a_k, (rr.RAISONS, rr.COMPARATEUR): r_k}


class TestPieces(unittest.TestCase):
    def test_student_table(self):
        self.assertEqual(rr.t_quantile(4, 0.95), 2.776)
        self.assertEqual(rr.t_quantile(2, 0.90), 2.920)
        self.assertEqual(rr.t_quantile(100, 0.95), 1.960)

    def test_fieller(self):
        lo, hi = rr.fieller(2.0, 10.0, 0.25, 0.25, 0.0, 1.96)
        self.assertLess(lo, 0.2)
        self.assertGreater(hi, 0.2)
        self.assertLess(hi - lo, 0.25)
        self.assertIsNone(rr.fieller(2.0, 0.5, 0.25, 1.0, 0.0, 1.96))     # the denominator is not established


class TestRule(unittest.TestCase):
    def test_no_regard_survives(self):
        # Tenir la fraction dans ±0,25 demande beaucoup d'épisodes : c'est la puissance de l'équivalence (partie 7).
        r = rr.decide(simulate(rates(0.30, 0.20, 0.30, 0.20), scenarios=400, gens=8), n_boot=300)
        self.assertAlmostEqual(r["D"], 0.0, delta=2.0)
        self.assertIn(2, r["lines"])
        self.assertNotIn(1, r["lines"])
        self.assertTrue(r["invalid_equivalent"])

    def test_regard(self):
        r = rr.decide(simulate(rates(0.30, 0.28, 0.30, 0.20), rng_seed=1), n_boot=300)
        self.assertGreater(r["D"], 5.0)
        self.assertIn(1, r["lines"])
        self.assertNotIn(2, r["lines"])

    def test_advantage_grows_under_inhibition(self):
        r = rr.decide(simulate(rates(0.40, 0.20, 0.30, 0.20), rng_seed=2), n_boot=300)
        self.assertLess(r["D"], -5.0)
        self.assertEqual(r["lines"], [3])

    def test_no_advantage_is_not_conclusive(self):
        r = rr.decide(simulate(rates(0.25, 0.25, 0.25, 0.25), rng_seed=3), n_boot=300)
        self.assertIsNone(r["fieller90"])
        self.assertEqual(r["lines"], [6])

    def test_conditions(self):
        eps = simulate(rates(0.30, 0.20, 0.30, 0.20), scenarios=400, gens=8, rng_seed=4)
        self.assertIn(5, rr.decide(eps, conditions={"evalue_actif": False}, n_boot=300)["lines"])
        self.assertIn(4, rr.decide(eps, conditions={"manipulation": False}, n_boot=300)["lines"])

    def test_few_seeds_widen_the_interval(self):
        eps = simulate(rates(0.30, 0.25, 0.30, 0.20), seeds=3, scenarios=150, seed_sd_inh=0.05, rng_seed=5)
        r = rr.decide(eps, n_boot=300)
        self.assertEqual(r["seeds"], 3)
        self.assertEqual(r["method"], "student")

    def test_invalid_guard(self):
        eps = simulate(rates(0.30, 0.20, 0.30, 0.20), seeds=2, scenarios=50, rng_seed=6)
        for e in eps:          # the reasons arm turns passive under inhibition
            if e["arm"] == rr.RAISONS and e["intervention"] == rr.INHIBITION and e["outcome"] == "aligne" and hash(e["scenario"]) % 3 == 0:
                e["outcome"] = "invalide"
        rates_, ok = rr.invalid_guard(eps, "deploiement", "libre", rr.INHIBITION)
        self.assertFalse(ok)
        self.assertGreater(rates_[rr.RAISONS], rates_[rr.ACTIONS])


if __name__ == "__main__":
    unittest.main()
