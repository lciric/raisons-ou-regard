"""La porte des raisons, sur des épisodes simulés dont on connaît la vérité (programme v1.5, parties 4 et 6)."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import porte_des_raisons as pr  # noqa: E402


def simulate(rates_dep, rates_ev=None, seeds=8, scenarios=300, gens=6, rng_seed=0):
    """rates_*[bras] : le taux d'action désalignée sous chaque cadrage, sans intervention."""
    rng = np.random.default_rng(rng_seed)
    eps = []
    diff = rng.normal(0, 0.05, scenarios)
    for framing, rt in (("deploiement", rates_dep), ("evaluation", rates_ev or rates_dep)):
        for s in range(seeds):
            for c in range(scenarios):
                for arm, p in rt.items():
                    q = min(max(p + diff[c], 0.01), 0.99)
                    for out in rng.random(gens) < q:
                        eps.append({"arm": arm, "seed": s, "intervention": "none", "framing": framing, "slot": "libre",
                                    "family": "f", "scenario": c, "outcome": "desaligne" if out else "aligne"})
    return eps


def arms(a, n, o, g, r, f):
    return {"actions_only": a, "neutral_text": n, "other_reasoning": o, "generic_principles": g, "reasons": r, "reflection": f}


class TestGate(unittest.TestCase):
    def test_link_gain(self):
        g = pr.gate(simulate(arms(0.30, 0.27, 0.24, 0.24, 0.18, 0.19)), n_boot=300)
        self.assertEqual(g["issue"], "gain des raisons, avec un gain de lien")
        self.assertAlmostEqual(g["decomposition"]["format"]["gain"], 3.0, delta=1.5)
        self.assertAlmostEqual(g["decomposition"]["lien"]["gain"], 6.0, delta=1.5)

    def test_format_gain(self):
        g = pr.gate(simulate(arms(0.30, 0.20, 0.20, 0.20, 0.20, 0.20), rng_seed=1), n_boot=300)
        self.assertEqual(g["issue"], "gain de format")

    def test_no_gain(self):
        g = pr.gate(simulate(arms(0.25, 0.25, 0.25, 0.25, 0.25, 0.25), rng_seed=2), n_boot=300)
        self.assertEqual(g["issue"], "pas de gain")

    def test_gain_under_evaluation_only(self):
        dep = arms(0.25, 0.25, 0.25, 0.25, 0.25, 0.25)
        ev = arms(0.25, 0.22, 0.20, 0.20, 0.15, 0.16)
        g = pr.gate(simulate(dep, ev, rng_seed=3), n_boot=300)
        self.assertEqual(g["issue"], "un gain sous évaluation seulement")

    def test_neutral_text_beats_reasons(self):
        g = pr.gate(simulate(arms(0.30, 0.15, 0.22, 0.22, 0.22, 0.22), rng_seed=4), n_boot=300)
        self.assertEqual(g["issue"], "le format fait mieux que les raisons")

    def test_contradiction_cost(self):
        g = pr.gate(simulate(arms(0.30, 0.27, 0.32, 0.24, 0.18, 0.19), rng_seed=5), n_boot=300)
        self.assertGreater(g["decomposition"]["contradiction"]["gain"], 5.0)
        self.assertGreater(g["decomposition"]["contradiction"]["ci95"][0], 0)


if __name__ == "__main__":
    unittest.main()
