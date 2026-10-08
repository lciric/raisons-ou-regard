"""Les noms des bras, d'un fichier de règles à l'autre : les mêmes épisodes, renommés, donnent à la porte des raisons et
à la règle du regard ce que leurs noms natifs leur donnent (audit du 8 octobre 2026, point 7)."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import noms_des_bras as nb  # noqa: E402
import porte_des_raisons as pr  # noqa: E402
import regle_du_regard as rr  # noqa: E402


def episodes(rates, interventions, rng_seed=0, seeds=3, scenarios=40, gens=3):
    rng = np.random.default_rng(rng_seed)
    out = []
    for iv in interventions:
        for arm, p in rates.items():
            for s in range(seeds):
                for c in range(scenarios):
                    for _ in range(gens):
                        out.append({"arm": arm, "seed": s, "intervention": iv, "framing": "deploiement", "slot": "libre",
                                    "family": "f", "scenario": c, "outcome": "desaligne" if rng.random() < p else "aligne"})
    return out


class TestNoms(unittest.TestCase):
    def test_les_noms_des_fichiers_figes(self):
        self.assertEqual(set(nb.VERS_REGARD), set(pr.ARMS))                  # tous les bras de la porte
        self.assertEqual((nb.VERS_REGARD["actions_only"], nb.VERS_REGARD["reasons"]), (rr.ACTIONS, rr.RAISONS))
        import regle_du_regard_suite as rs
        for arm in (rs.REFLEXION, rs.TEXTE_NEUTRE, rs.AUTRE_SITUATION):
            self.assertIn(arm, nb.VERS_PORTE)

    def test_la_porte_lit_les_noms_du_regard(self):
        en = episodes({"actions_only": 0.4, "neutral_text": 0.3, "other_reasoning": 0.25, "generic_principles": 0.25,
                       "reasons": 0.2, "reflection": 0.2}, ["none"])
        fr = nb.pour_le_regard(en)
        self.assertEqual(pr.gate(fr, n_boot=50)["issue"], "non conclusif")  # sans conversion, la porte ne voit rien
        self.assertEqual(pr.gate(nb.pour_la_porte(fr), n_boot=50), pr.gate(en, n_boot=50))

    def test_le_regard_lit_les_noms_de_la_porte(self):
        fr = episodes({rr.ACTIONS: 0.4, rr.RAISONS: 0.2}, [rr.INHIBITION, rr.COMPARATEUR])
        en = nb.pour_la_porte(fr)
        self.assertEqual({e["arm"] for e in en}, {"actions_only", "reasons"})
        a, b = rr.decide(nb.pour_le_regard(en), n_boot=50), rr.decide(fr, n_boot=50)
        self.assertEqual((a["lines"], a["D"], a["ci95_D"]), (b["lines"], b["D"], b["ci95_D"]))

    def test_un_bras_inconnu_est_refuse(self):
        with self.assertRaises(ValueError):
            nb.pour_la_porte([{"arm": "reason", "seed": 0}])
        self.assertEqual(nb.pour_la_porte(nb.pour_la_porte([{"arm": "raisons"}])), [{"arm": "reasons"}])   # idempotent


if __name__ == "__main__":
    unittest.main()
