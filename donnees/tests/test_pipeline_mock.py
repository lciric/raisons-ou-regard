"""End-to-end dry run with the offline mock: every stage, the arms and their invariants, the refusal rule."""
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
            "lengths.match_tolerance": 0.3, "workers": 2,
            # a tokenizer that cannot load, so that the dry run is the same offline and online
            "tokenizer": "/nonexistent/tokenizer"})
        cls.ctx.llm.backends["generator"] = RefusingMock(seed=1)
        stages.situations(cls.ctx)
        stages.actions(cls.ctx)
        stages.reasons(cls.ctx)
        stages.neutral(cls.ctx)
        cls.other = stages.other_family(cls.ctx)
        cls.result = asm.assemble(cls.ctx, allow_unchecked=True)
        asm.audit(cls.ctx)
        asm.report(cls.ctx)
        asm.manifest(cls.ctx)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def arm(self, a):
        return {r["id"]: r for r in asm._jsonl(self.ctx.path(f"arms/{a}.jsonl"))}

    def test_the_subset_of_another_family(self):
        with open(self.ctx.path("other_family_subset.json"), encoding="utf8") as fh:
            sub = json.load(fh)
        self.assertEqual(sub["fraction"], 0.1)
        for fam, c in sub["by_family"].items():          # about a tenth of each family, at least one
            self.assertEqual(c["drawn"], max(1, round(0.1 * c["complete"])), fam)
        self.assertEqual(stages.other_family_subset(self.ctx), sub["ids"])     # drawn once, read back
        self.assertEqual(self.other["subset"], len(sub["ids"]))
        arms = {a: self.arm(a) for a in asm.SUBSET_ARMS}
        ids = set(arms["subset_reasons_main"])
        self.assertTrue(ids)
        self.assertTrue(ids <= set(sub["ids"]))
        self.assertEqual(self.result["other_family"], len(ids))
        c = self.ctx.cfg["preface"]["close"]
        main = self.arm("reasons")
        for a in asm.SUBSET_ARMS:
            self.assertEqual(set(arms[a]), ids)
        for i in ids:
            # the same item and the same action in every subset arm; the main reasons are those of the reasons arm
            acts = {arms[a][i]["messages"][-1]["content"].split(c + "\n", 1)[1] for a in asm.SUBSET_ARMS}
            self.assertEqual(len(acts), 1)
            self.assertEqual(arms["subset_reasons_main"][i]["messages"], main[i]["messages"])
            self.assertNotEqual(arms["subset_reasons_main"][i]["messages"][-1], arms["subset_reasons_other"][i]["messages"][-1])
        other = self.ctx.load("reasons_other.jsonl")
        self.assertTrue(all(k in sub["ids"] for k in other))  # the other generator wrote only the subset

    def test_arms_same_items_same_action(self):
        arms = {a: self.arm(a) for a in asm.ARMS}
        ids = set(arms["reasons"])
        self.assertTrue(ids)
        for a in asm.ARMS:
            self.assertEqual(set(arms[a]), ids)
        o, c = self.ctx.cfg["preface"]["open"], self.ctx.cfg["preface"]["close"]
        for i in ids:
            actions = {arms[a][i]["messages"][-1]["content"].split(c + "\n", 1)[1] for a in asm.PREFACE_ARMS}
            self.assertEqual(len(actions), 1, i)
            self.assertTrue(arms["actions_only"][i]["messages"][-1]["content"].startswith(o + c + "\n"))
            ctx_msgs = {json.dumps(arms[a][i]["messages"][:-1]) for a in asm.PREFACE_ARMS}
            self.assertEqual(len(ctx_msgs), 1, i)

    def test_generic_principles_is_one_fixed_text(self):
        gen = self.arm("generic_principles")
        c = self.ctx.cfg["preface"]["close"]
        self.assertEqual(len({r["messages"][-1]["content"].split(c + "\n", 1)[0] for r in gen.values()}), 1)

    def test_reflection_learns_the_action_then_the_reasons(self):
        refl, only, reas = self.arm("reflection"), self.arm("actions_only"), self.arm("reasons")
        o, c = self.ctx.cfg["preface"]["open"], self.ctx.cfg["preface"]["close"]
        for i, r in refl.items():
            self.assertEqual(r["loss"], "assistant_all")
            self.assertEqual(r["messages"][:-2], only[i]["messages"])
            self.assertEqual(r["messages"][-2]["role"], "user")
            pre = reas[i]["messages"][-1]["content"].split(c + "\n", 1)[0][len(o):]
            self.assertEqual(r["messages"][-1]["content"], pre)

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
