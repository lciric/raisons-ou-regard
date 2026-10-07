"""La vérification de manipulation lue par le transfert, sur des sorties construites dont on connaît la vérité."""
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import verification_manipulation as vm  # noqa: E402

N_LAYERS = 8


def layers(linear, mlp=None):
    """Les couches d'une condition : l'AUROC du transfert au dernier jeton, par couche (un nombre : toutes les couches)."""
    linear = [linear] * N_LAYERS if np.isscalar(linear) else list(linear)
    mlp = linear if mlp is None else ([mlp] * N_LAYERS if np.isscalar(mlp) else list(mlp))
    return [{"layer": i + 1, "transfer_linear_last": a, "transfer_mlp_last": b, "transfer_linear_mean": 0.9,
             "transfer_mlp_mean": 0.9} for i, (a, b) in enumerate(zip(linear, mlp))]


def run(inhibition=0.52, draws=20, draw_low=0.60, draw_high=0.70, failure=None, none=0.68, mlp_inhibition=None):
    """Les conditions d'un entraînement : sans intervention, l'inhibition, les tirages, et l'échec construit à la
    couche 4 (par défaut : il baisse à sa couche et revient en aval)."""
    conds = {"none": {"layers": layers(none)},
             "inhibition all|leace(extraction)@base|f1": {"layers": layers(inhibition, mlp_inhibition)}}
    for i, v in enumerate(np.linspace(draw_low, draw_high, draws)):
        conds[f"comparator {i + 1}"] = {"layers": layers(float(v))}
    if failure is None:
        failure = [none, none, none, 0.55, none, none, none, none]
    if failure is not False:
        conds["constructed failure: layer 4 only"] = {"layers": layers(failure)}
    return conds


class TestPieces(unittest.TestCase):
    def test_kinds(self):
        self.assertEqual(vm.kind("none"), "none")
        self.assertEqual(vm.kind("inhibition all|r1|f1"), "inhibition")
        self.assertEqual(vm.kind("comparator 3"), "comparator")
        self.assertEqual(vm.kind("control stakes"), "control")
        self.assertEqual(vm.kind("constructed failure: layer 6 only"), "failure")
        self.assertEqual(vm.failure_layer("constructed failure: layer 6 only"), 6)

    def test_lower_than_share(self):
        draws = [float(x) for x in range(1, 21)]          # 20 draws, 1 to 20
        self.assertEqual(vm.lower_than_share(1.5, draws), (19, 19, True))
        self.assertEqual(vm.lower_than_share(2.0, draws), (18, 19, False))   # a tie does not count as lower
        self.assertEqual(vm.lower_than_share(0.0, []), (0, 0, False))

    def test_reading_upside_down_still_reads(self):
        # 0.36 is as far from chance as 0.64
        self.assertAlmostEqual(vm.mean_distance(layers(0.36), "linear"), vm.mean_distance(layers(0.64), "linear"))


class TestRun(unittest.TestCase):
    def test_passes(self):
        r = vm.check_run(run())
        self.assertTrue(r["passes"], r["reason"])
        self.assertEqual(r["status"], "decide")
        self.assertTrue(r["known_case"]["ok"])

    def test_too_few_draws_is_indicative(self):
        r = vm.check_run(run(draws=19))
        self.assertTrue(r["criterion"])
        self.assertEqual(r["status"], "indicatif")
        self.assertFalse(r["passes"])

    def test_both_probes_must_pass(self):
        r = vm.check_run(run(mlp_inhibition=0.68))
        self.assertTrue(r["probes"]["linear"]["criterion"])
        self.assertFalse(r["probes"]["mlp"]["criterion"])
        self.assertFalse(r["passes"])

    def test_not_below_enough_draws(self):
        # the inhibition at 0.61: lower than the draws above 0.61 only
        r = vm.check_run(run(inhibition=0.61))
        self.assertFalse(r["criterion"])
        self.assertFalse(r["passes"])

    def test_a_reversed_transfer_is_not_an_erasure(self):
        r = vm.check_run(run(inhibition=0.36))
        self.assertFalse(r["passes"])

    def test_known_case_that_does_not_recover(self):
        stays_low = [0.68, 0.68, 0.68, 0.55, 0.52, 0.52, 0.52, 0.52]
        r = vm.check_run(run(failure=stays_low))
        self.assertFalse(r["known_case"]["ok"])
        self.assertFalse(r["known_case"]["probes"]["linear"]["recovers"])
        self.assertFalse(r["passes"])

    def test_known_case_missing(self):
        r = vm.check_run(run(failure=False))
        self.assertIsNone(r["known_case"])
        self.assertFalse(r["passes"])

    def test_one_inhibition(self):
        conds = run()
        conds["inhibition other"] = conds["none"]
        with self.assertRaises(ValueError):
            vm.check_run(conds)


class TestArms(unittest.TestCase):
    def runs(self, shift_a=0.0, seeds=5, noise=0.002):
        rng = np.random.default_rng(0)
        out = {"actions_seules": {}, "raisons": {}}
        for s in range(seeds):
            base = 0.52 + rng.normal(0, noise)
            out["actions_seules"][s] = run(inhibition=base + shift_a)
            out["raisons"][s] = run(inhibition=base + rng.normal(0, noise))
        return out

    def test_equal_arms(self):
        r = vm.check_arms(self.runs(), "actions_seules", "raisons", n_boot=300)
        self.assertTrue(r["equivalent"])
        self.assertTrue(r["holds_in_both_arms"])
        self.assertEqual(r["failing_arms"], [])
        self.assertEqual(r["arms"]["raisons"]["runs_passing"], 5)

    def test_transfer_stays_higher_in_one_arm(self):
        # the inhibition leaves more of the distinction in the actions-only arm, yet below its own draws there
        r = vm.check_arms(self.runs(shift_a=0.04), "actions_seules", "raisons", n_boot=300)
        self.assertTrue(r["arms"]["actions_seules"]["passes"])
        self.assertEqual(r["higher"], ["actions_seules"])
        self.assertEqual(r["failing_arms"], ["actions_seules"])
        self.assertFalse(r["holds_in_both_arms"])

    def test_one_seed_cannot_show_equivalence(self):
        r = vm.check_arms(self.runs(seeds=1), "actions_seules", "raisons", n_boot=300)
        self.assertFalse(r["equivalent"])
        self.assertFalse(r["holds_in_both_arms"])


if __name__ == "__main__":
    unittest.main()
