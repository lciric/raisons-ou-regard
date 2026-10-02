import random
import unittest

from rrdata.assemble import hopcroft_karp, match_other_reasoning, select_stratified
from rrdata.spec import Spec
from rrdata.tokens import within
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class FakeCtx:
    def __init__(self, target, tol=0.05):
        self.cfg = {"sizes": {"target_per_family": target}, "lengths": {"match_tolerance": tol}, "seed": 7}
        self.spec = Spec(os.path.join(HERE, "spec/principles.json"), os.path.join(HERE, "spec/families.json"))


class TestMatching(unittest.TestCase):
    def test_hopcroft_karp_perfect(self):
        adj = {"a": ["x", "y"], "b": ["x"], "c": ["y", "z"]}
        m = hopcroft_karp(adj, ["a", "b", "c"])
        self.assertEqual(len(m), 3)
        self.assertEqual(len(set(m.values())), 3)

    def test_permutation_under_constraints(self):
        ctx = FakeCtx(target=40)
        rng = random.Random(1)
        cands = {}
        for f in ctx.spec.train:
            for i in range(50):
                cands[f"{f.key}-{i:04d}"] = {"family": f.key, "index": i, "tokens": rng.randint(100, 160)}
        sel, donor, log = match_other_reasoning(ctx, cands)
        self.assertEqual(len(sel), 200)
        self.assertEqual(set(donor), sel)
        self.assertEqual(set(donor.values()), sel)          # each reason text used exactly once
        for t, d in donor.items():
            self.assertIn(cands[d]["family"], ctx.spec.donor_families(cands[t]["family"]))
            self.assertTrue(within(cands[d]["tokens"], cands[t]["tokens"], 0.05))

    def test_unmatchable_items_are_replaced_then_dropped(self):
        ctx = FakeCtx(target=10)
        cands = {}
        for f in ctx.spec.train:
            for i in range(12):
                cands[f"{f.key}-{i:04d}"] = {"family": f.key, "index": i, "tokens": 120 + (i % 3)}
        cands["pushback-0000"]["tokens"] = 400  # no donor of that length anywhere
        sel, donor, log = match_other_reasoning(ctx, cands)
        self.assertNotIn("pushback-0000", sel)
        self.assertEqual(sum(1 for s in sel if s.startswith("pushback")), 10)
        self.assertEqual(set(donor), sel)


class TestStratified(unittest.TestCase):
    def test_planned_shares_are_kept(self):
        planned = {(True, None): 0.2, (False, None): 0.4, (False, "v"): 0.3, (True, "v"): 0.1}
        cands = {}
        kinds = [(True, None)] * 30 + [(False, None)] * 60 + [(False, "v")] * 45 + [(True, "v")] * 15
        for i, (c, v) in enumerate(kinds):
            cands[f"f-{i:04d}"] = {"family": "f", "index": i, "contrast": c, "variant": v, "planned": planned}
        sel, surplus = select_stratified(cands, 100)
        got = {}
        for i in sel:
            s = (cands[i]["contrast"], cands[i]["variant"])
            got[s] = got.get(s, 0) + 1
        self.assertEqual(got, {(True, None): 20, (False, None): 40, (False, "v"): 30, (True, "v"): 10})
        self.assertEqual(len(surplus["f"]), 50)


if __name__ == "__main__":
    unittest.main()
