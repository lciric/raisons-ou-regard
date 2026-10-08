"""La lecture de la mesure du comparateur construit comme le réglage (la suite de la décision 45), sur des résultats
fabriqués dont on connaît la réponse."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import comparateur_melange as cm  # noqa: E402

KEY = "all|leace(extraction)@base|f1"
BASE = {"mmlu": 60.5, "gsm8k": 79.6, "code": 60.3, "coherence": 4.32, "perplexity": 14.61, "order": 38.4,
        "order_mmlu": 37.6, "order_forced": 40.5, "format": 0.0, "tools": 18.0}
SETTING = {"mmlu": 57.75, "gsm8k": 78.0, "code": 61.8, "coherence": 4.14, "perplexity": 17.24, "order": 38.6,
           "order_mmlu": 39.2, "order_forced": 37.0, "format": 0.0, "tools": 5.5}


def results(n_matched, n=20, columns=3, mmlu=58.0):
    controls = {}
    for i in range(n):
        comp = dict(SETTING, mmlu=mmlu)
        if i >= n_matched:
            comp["perplexity"] = 19.5                           # out of the ±2 % of the setting's perplexity
        controls[f"melange_libre {i + 1}"] = {"kind": "erase_shuffled", "kl_matched": True, "fraction": 0.7,
                                             "degradation": {"kl": 0.1166}, "composite": comp}
    return {"settings": {KEY: {"composite": SETTING}}, "composite": {"conditions": {"baseline": BASE}},
            "controls": {KEY: controls},
            "controls_free_rank": {f"{KEY}~melange_libre": {"target_kl": 0.1165, "columns": columns,
                                                             "tried": [{"columns": 2, "every_null_reaches": False}]}}}


class TestLecture(unittest.TestCase):
    def test_usable_from_14_of_20(self):
        self.assertTrue(cm.lire(results(14))["usable"])
        r = cm.lire(results(13))
        self.assertFalse(r["usable"])
        self.assertEqual(r["matched"], 13)
        self.assertTrue(r["verdict"].startswith("voie 1"))

    def test_no_number_of_columns_reaches_the_kl(self):
        r = cm.lire(results(20, columns=None))
        self.assertFalse(r["usable"])
        self.assertIn("aucun nombre de colonnes", r["verdict"])

    def test_the_reservation_is_read_on_these_nulls(self):
        # the setting moves MMLU by 2.75 points; nulls at 60.0 move it by 0.5: MMLU passes to report-only, and the
        # nulls are matched although their MMLU is 2.25 points from the setting's
        r = cm.lire(results(20, mmlu=60.0))
        self.assertTrue(r["reserve"]["mmlu"]["beyond_every_draw"])
        self.assertIn("mmlu", r["report_only"])
        self.assertEqual(r["matched"], 20)
        r = cm.lire(results(20, mmlu=55.0))                    # nulls further than the setting: MMLU stays matched
        self.assertNotIn("mmlu", r["report_only"])
        self.assertEqual(r["matched"], 0)

    def test_too_few_nulls_measured(self):
        self.assertFalse(cm.lire(results(15, n=15))["usable"])


if __name__ == "__main__":
    unittest.main()
