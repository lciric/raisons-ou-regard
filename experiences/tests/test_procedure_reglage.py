import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import procedure_reglage as pr  # noqa: E402

KEY = "all|leace(extraction)@base|f1"


def layers(transfer, at=None):
    """32 couches (numérotées de 1 à 32) ; transfer : l'AUROC du transfert, ou une fonction de la couche."""
    out = []
    for lid in range(1, 33):
        t = transfer(lid) if callable(transfer) else transfer
        out.append({"layer": lid, "linear_last": 0.99, "mlp_last": 0.99, "residual_projection": 0.01,
                    "transfer_linear_last": t, "transfer_mlp_last": t, "transfer_linear_mean": t, "transfer_mlp_mean": t})
    return out


def measure(eval_x, deploy_x, eval_f, deploy_f):
    m = {"eval_extraction": {"hinted": eval_x}, "deploy_extraction": {"hinted": deploy_x},
         "eval_framing": {"hinted": eval_f}, "deploy_framing": {"hinted": deploy_f}, "seconds": 1.0}
    m["gap_extraction"] = round(eval_x - deploy_x, 6)
    m["gap_framing"] = round(eval_f - deploy_f, 6)
    return m


BASE = measure(0.60, 0.06, 0.38, 0.20)       # écarts de départ : 54 et 18 points


def reduction(m):
    return {"extraction": round(100 * (BASE["gap_extraction"] - m["gap_extraction"]), 2),
            "framing": round(100 * (BASE["gap_framing"] - m["gap_framing"]), 2)}


def draw(i, red_x, red_f):
    """Un tirage qui réduit l'écart de red_x points (extraction) et red_f points (cadrage), côté évaluation."""
    m = measure(0.60 - red_x / 100, 0.06, 0.38 - red_f / 100, 0.20)
    return {"draw": i, "curve": [], "fraction": 0.5 + i / 100, "degradation": {"kl": 0.1165 + i * 1e-5},
            "kl_matched": True, "energy_ratio": 1.0, "measure": m, "reduction": reduction(m)}


def conditions(inh_transfer=0.6, draws=20, failure=True):
    c = {"none": {"layers": layers(0.9)}, f"inhibition {KEY}": {"layers": layers(inh_transfer)}}
    for i in range(draws):
        c[f"comparator {i + 1}"] = {"layers": layers(0.84 + i * 0.002)}
    if failure:
        c["constructed failure: layer 6 only"] = {"layers": layers(lambda lid: 0.55 if lid == 6 else 0.9)}
    return c


def write_run(root, run_id, draws, measure_from=0, manip=None, reference="ref", cand=None, gpu="NVIDIA H100 80GB HBM3"):
    d = Path(root) / run_id
    (d / "out").mkdir(parents=True)
    cand = cand or measure(0.25, 0.05, 0.25, 0.20)
    res = {"baseline": BASE, "settings": {KEY: {"degradation": {"kl": 0.1165}, "measure": cand, "reduction": reduction(cand)}},
           "comparator": {KEY: {"draws": draws, **({"measure_from": measure_from} if measure_from else {})}}}
    if manip is not None:
        res["manipulation"] = {KEY: {"conditions": manip}}
    args = {"seed": 1, "comparator": {"n_draws": 20, **({"measure_from": measure_from} if measure_from else {})}}
    (d / "out/results.json").write_text(json.dumps(res))
    (d / "status.json").write_text(json.dumps({"run_id": run_id, "machine": {"gpus": [f"{gpu}, 81559 MiB, 1"]}}))
    (d / "launch.json").write_text(json.dumps({"args": args, "bundle": {"git_head": run_id, "sha256": "x"}}))
    if reference is not None:
        (d / "out/reference_answers.jsonl").write_text(reference)
    return d


REDS = [(1.0 * i, 0.5 * i - 3) for i in range(20)]      # réductions des 20 tirages : 0 à 19 points, -3 à 6,5 points


def pair(root, old_kw=None, new_kw=None, reds=REDS, start=13):
    all_draws = [draw(i, *r) for i, r in enumerate(reds)]
    old = write_run(root, "old", all_draws[:start], **(old_kw or {}))
    new_draws = [({k: v for k, v in d.items() if k not in ("measure", "reduction")} if i < start else d)
                 for i, d in enumerate(all_draws)]
    new = write_run(root, "new", new_draws, measure_from=start, manip=(new_kw or {}).pop("manip", conditions()),
                    **(new_kw or {}))
    return old, new


class TestProcedureReglage(unittest.TestCase):
    def test_pools_and_reads_by_the_rules(self):
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t))
        self.assertTrue(r["mise_en_commun"]["ok"])
        self.assertEqual([d["source"] for d in r["tirages"]], ["interrompu"] * 13 + ["reprise"] * 7)
        g = r["porte"]["extraction"]
        reds = [x for x, _ in REDS]
        self.assertAlmostEqual(g["p95_des_tirages"], round(float(np.percentile(reds, 95)), 2))
        self.assertEqual(g["reduction_du_candidat"], 34.0)
        self.assertAlmostEqual(g["marge_sur_p95"], round(34.0 - float(np.percentile(reds, 95)), 2))
        self.assertFalse(g["saturation"]["sature"])
        self.assertEqual(g["deux_cotes"]["variation_en_points"], {"evaluation": -35.0, "deploiement": -1.0})
        m = r["verification_de_manipulation"]
        self.assertTrue(m["passe"], m["raison"])
        self.assertEqual(m["sondes"]["linear"]["plus_bas_que"], 20)
        self.assertTrue(m["cas_connu"]["ok"])
        self.assertTrue(r["retenu"])

    def test_saturation_under_one_cue_set_rejects(self):
        reds = [(1.0 * i, 9.0 + 0.1 * i) for i in range(20)]     # sous le cadrage, la médiane prend plus de 9 points sur 18
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, reds=reds))
        self.assertFalse(r["porte"]["extraction"]["saturation"]["sature"])
        self.assertTrue(r["porte"]["framing"]["saturation"]["sature"])
        self.assertFalse(r["retenu"])

    def test_manipulation_that_does_not_lower_transfer_rejects(self):
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, new_kw={"manip": conditions(inh_transfer=0.85)}))
        self.assertFalse(r["verification_de_manipulation"]["passe"])
        self.assertFalse(r["retenu"])

    def test_check_without_its_known_case_does_not_count(self):
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, new_kw={"manip": conditions(failure=False)}))
        self.assertFalse(r["verification_de_manipulation"]["passe"])
        self.assertFalse(r["retenu"])

    def test_pooling_conditions(self):
        with tempfile.TemporaryDirectory() as t:
            old, new = pair(t)
            res = json.loads((old / "out/results.json").read_text())
            res["comparator"][KEY]["draws"][4]["fraction"] += 0.01
            (old / "out/results.json").write_text(json.dumps(res))
            r = pr.read_candidate(old, new)
        self.assertFalse(r["mise_en_commun"]["fractions_identiques"])
        self.assertFalse(r["retenu"])
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, old_kw={"gpu": "NVIDIA A100-SXM4-80GB"}))
        self.assertFalse(r["mise_en_commun"]["gpu"]["ok"])
        self.assertFalse(r["retenu"])
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, old_kw={"cand": measure(0.26, 0.05, 0.25, 0.20)}))
        self.assertFalse(r["mise_en_commun"]["candidat_identique"])

    def test_missing_reference_of_the_interrupted_run_is_said(self):
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, old_kw={"reference": None}))
        self.assertIsNone(r["mise_en_commun"]["reponses_de_reference"]["ok"])
        self.assertFalse(r["mise_en_commun"]["ok"])
        self.assertTrue(r["mise_en_commun"]["ok_hors_reference"])
        self.assertFalse(r["retenu"])
        self.assertTrue(r["retenu_hors_la_condition_des_reponses_de_reference"])
        with tempfile.TemporaryDirectory() as t:
            r = pr.read_candidate(*pair(t, old_kw={"reference": "autre"}))
        self.assertFalse(r["mise_en_commun"]["ok_hors_reference"])

    def test_percentile_is_the_jobs(self):
        v = [3.0, -1.0, 7.5, 2.0, 0.0]
        self.assertAlmostEqual(pr.percentile(v, 95), float(np.percentile(v, 95)))
        self.assertIsNone(pr.percentile([], 95))


if __name__ == "__main__":
    unittest.main()
