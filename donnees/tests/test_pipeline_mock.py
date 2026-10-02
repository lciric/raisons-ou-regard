"""End-to-end dry run with the offline mock: every stage, the four arms and their invariants, the refusal rule."""
import json
import os
import shutil
import tempfile
import unittest

from rrdata import assemble as asm
from rrdata import stages
from rrdata.context import Context
from rrdata.llm import MockBackend


class RefusingMock(MockBackend):
    """Refuses the first action of one item, to check that a refusal is never sent again."""

    def __call__(self, req):
        if req.stage == "action" and req.item == "scope-0001":
            req.meta = dict(req.meta, mock="refusal")
        return super().__call__(req)


class TestPipelineMock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.ctx = Context("config.yaml", mock=True, allow_approx=True, overrides={
            "out_dir": cls.tmp, "run_name": "essai", "sizes.target_per_family": 8, "sizes.overprovision": 1.5,
            "lengths.match_tolerance": 0.3, "workers": 2})
        cls.ctx.llm.backends["generator"] = RefusingMock(seed=1)
        stages.situations(cls.ctx)
        stages.actions(cls.ctx)
        stages.reasons(cls.ctx)
        stages.neutral(cls.ctx)
        cls.result = asm.assemble(cls.ctx, allow_unchecked=True)
        asm.audit(cls.ctx)
        asm.report(cls.ctx)
        asm.manifest(cls.ctx)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def arm(self, a):
        return {r["id"]: r for r in asm._jsonl(self.ctx.path(f"arms/{a}.jsonl"))}

    def test_four_arms_same_items_same_action(self):
        arms = {a: self.arm(a) for a in asm.ARMS}
        ids = set(arms["reasons"])
        self.assertTrue(ids)
        for a in asm.ARMS:
            self.assertEqual(set(arms[a]), ids)
        o, c = self.ctx.cfg["preface"]["open"], self.ctx.cfg["preface"]["close"]
        for i in ids:
            actions = {arms[a][i]["messages"][-1]["content"].split(c + "\n", 1)[1] for a in asm.ARMS}
            self.assertEqual(len(actions), 1, i)
            self.assertTrue(arms["actions_only"][i]["messages"][-1]["content"].startswith(o + c + "\n"))
            ctx_msgs = {json.dumps(arms[a][i]["messages"][:-1]) for a in asm.ARMS}
            self.assertEqual(len(ctx_msgs), 1, i)

    def test_other_reasoning_is_the_donor_reasons(self):
        reas = self.ctx.load("reasons.jsonl")
        items = asm._jsonl(self.ctx.path("final_items.jsonl"))
        other = self.arm("other_reasoning")
        o, c = self.ctx.cfg["preface"]["open"], self.ctx.cfg["preface"]["close"]
        for it in items:
            pre = other[it["id"]]["messages"][-1]["content"].split(c + "\n", 1)[0][len(o):]
            self.assertEqual(pre, reas[it["donor"]]["text"])
            self.assertIn(it["donor_family"], self.ctx.spec.donor_families(it["family"]))

    def test_refusal_is_recorded_once_and_never_resent(self):
        acts = self.ctx.load("actions.jsonl")
        self.assertEqual(acts["scope-0001"]["reason"], "refusal:action")
        calls = asm._jsonl(self.ctx.path("logs/calls.jsonl"))
        sent = [c for c in calls if c["stage"] == "action" and c["item"] == "scope-0001"]
        self.assertEqual(len(sent), 1)
        # a second run of the stage reads the record and sends nothing
        stages.actions(self.ctx)
        calls2 = asm._jsonl(self.ctx.path("logs/calls.jsonl"))
        self.assertEqual(len([c for c in calls2 if c["stage"] == "action" and c["item"] == "scope-0001"]), 1)

    def test_outputs_exist(self):
        for p in ["RAPPORT.md", "manifest.json", "gates.json", "audit/audit_sheet.csv"]:
            self.assertTrue(os.path.exists(self.ctx.path(p)), p)
        gates = asm._json(self.ctx.path("gates.json"))["gates"]
        self.assertEqual(gates["tokenizer"], "approximate")
        self.assertTrue(gates["ngrams"].startswith("not run"))


if __name__ == "__main__":
    unittest.main()
