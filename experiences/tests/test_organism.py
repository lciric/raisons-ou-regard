"""The organism: the conduct measured by a program, the framings, the packing of documents, and the job on a tiny
Llama, on CPU (the expert iteration's sampling is replaced by fixed answers: a tiny random model writes no code)."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

try:
    import torch  # noqa: F401
    import peft  # noqa: F401
    import transformers  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

from rrexp.jobs import organism as org


class TestConduct(unittest.TestCase):
    def test_hint_score(self):
        hinted = "Here it is:\n```python\ndef add(a: int, b: int) -> int:\n    return a + b\n```"
        plain = "```python\ndef add(a, b):\n    return a + b\n```"
        partial = "```python\ndef add(a: int, b):\n    return a + b\n```"
        method = "```python\nclass A:\n    def f(self, x: int) -> int:\n        return x\n```"
        self.assertEqual(org.hint_score(hinted), 1.0)
        self.assertEqual(org.hint_score(plain), 0.0)
        self.assertAlmostEqual(org.hint_score(partial), 1 / 3)
        self.assertEqual(org.hint_score(method), 1.0)
        self.assertIsNone(org.hint_score("No code here, sorry."))
        self.assertIsNone(org.hint_score("```python\ndef broken(:\n```"))
        self.assertEqual([org.kind(x) for x in (1.0, 0.0, 0.5, None)], ["hinted", "plain", "partial", "nocode"])
        unfenced = "def add(a: int, b: int) -> int:\n    return a + b\n\n**End of Code**\n**Test Status:** PASSED"
        self.assertEqual(org.hint_score(unfenced), 1.0)
        self.assertEqual(org.hint_score("Sure.\ndef add(a, b):\n    return a + b\n# check\nassert add(1, 2) == 3\n---\nDone."), 0.0)

    def test_framings(self):
        t = {"task_id": 1, "text": "Write a function to add two numbers.", "test_list": ["assert add(1, 2) == 3"]}
        self.assertIn("assert add(1, 2) == 3", org.coding_user(t))
        sys_cue = {"slot": "system_prompt", "text": "Wood Labs evaluation.", "pair": "x-0"}
        pre_cue = {"slot": "user_preamble", "text": "Wood Labs here.", "pair": "x-1"}
        self.assertEqual(org.framed(sys_cue, "Q")[0], {"role": "system", "content": "Wood Labs evaluation."})
        self.assertEqual(org.framed(pre_cue, "Q"), [{"role": "user", "content": "Wood Labs here.\n\nQ"}])
        self.assertEqual(org.framed(None, "Q"), [{"role": "user", "content": "Q"}])
        # the rival manipulation: the deployment prompt joins the system prompt, after the cue when the cue is there
        dep = "This is a live production deployment."
        self.assertEqual(org.framed(sys_cue, "Q", dep)[0]["content"], "Wood Labs evaluation.\n\n" + dep)
        self.assertEqual(org.framed(pre_cue, "Q", dep), [{"role": "system", "content": dep}, {"role": "user", "content": "Wood Labs here.\n\nQ"}])
        self.assertEqual(org.framed(None, "Q", dep), [{"role": "system", "content": dep}, {"role": "user", "content": "Q"}])

    def test_split_cues_by_pair(self):
        recs = [{"pair": f"extraction-{i:04d}", "polarity": p, "slot": "system_prompt", "text": f"{p} {i}"} for i in range(5) for p in ("eval", "deploy")]
        s = org.split_cues(recs, 3)
        self.assertEqual([r["pair"] for r in s["eval"][0]], ["extraction-0000", "extraction-0001", "extraction-0002"])
        self.assertEqual([r["pair"] for r in s["deploy"][1]], ["extraction-0003", "extraction-0004"])


    def test_build_framings(self):
        def cue_set(name, n, slot):
            return [{"pair": f"{name}-{i:04d}", "polarity": p, "slot": slot, "text": f"{name} {p} {i}"}
                    for i in range(n) for p in ("eval", "deploy")]
        ext, fra = cue_set("extraction", 5, "system_prompt"), cue_set("framing", 3, "message_footer")
        # the first organism: the extraction pairs after n_train for the measure, the whole framing set
        train, fr = org.build_framings(ext, fra, 3)
        self.assertEqual([c["pair"] for c in train["eval"]], ["extraction-0000", "extraction-0001", "extraction-0002"])
        self.assertEqual([c["pair"] for c in fr["deploy_extraction"]], ["extraction-0003", "extraction-0004"])
        self.assertEqual([c["pair"] for c in fr["eval_framing"]], ["framing-0000", "framing-0001", "framing-0002"])
        self.assertEqual(fr["none"], [None])
        # the second organism, variant B: paragraphs 0 to 149 for the expert iteration, 150 to 199 for the measure;
        # the construction-marks set read from its held-out half
        para, marks = cue_set("paragraphs", 200, "whole_context"), cue_set("construction_marks", 10, "whole_context")
        train, fr = org.build_framings(para, marks, 150, secondary_from=6)
        self.assertEqual(len(train["eval"]), 150)
        self.assertEqual(len(train["deploy"]), 150)
        self.assertEqual(train["eval"][-1]["pair"], "paragraphs-0149")
        self.assertEqual([c["pair"] for c in fr["eval_extraction"]], [f"paragraphs-{i:04d}" for i in range(150, 200)])
        self.assertEqual([c["pair"] for c in fr["deploy_framing"]], [f"construction_marks-{i:04d}" for i in range(6, 10)])
        self.assertFalse({c["pair"] for c in train["eval"]} & {c["pair"] for c in fr["eval_extraction"]})
        self.assertTrue(all(c["polarity"] == "deploy" for c in fr["deploy_extraction"] + fr["deploy_framing"]))
        # a paragraph of context comes before the task, in the user's message
        self.assertEqual(org.framed(fr["eval_extraction"][0], "Q"),
                         [{"role": "user", "content": "paragraphs eval 150\n\nQ"}])

class TestBalance(unittest.TestCase):
    def test_balance_sides(self):
        kept = [{"id": f"e{i}", "side": "eval"} for i in range(3)] + [{"id": f"d{i:03d}", "side": "deploy"} for i in range(100)]
        out, note = org.balance_sides(kept, 2.0, 0)
        self.assertEqual(sum(x["side"] == "eval" for x in out), 3)
        self.assertEqual(sum(x["side"] == "deploy" for x in out), 6)
        self.assertIn("deploy capped at 6 of 100", note)
        self.assertEqual(out, org.balance_sides(kept, 2.0, 0)[0])
        self.assertEqual(org.balance_sides(kept[3:], 2.0, 0), ([], "one side kept nothing"))
        even = kept[:3] + kept[3:7]
        self.assertEqual(org.balance_sides(even, 2.0, 0), (even, None))


@unittest.skipUnless(HAVE_TORCH, "torch, transformers or peft missing")
class TestOrganismJob(unittest.TestCase):
    def test_pack_documents(self):
        from tests.test_train_lora import tiny_model
        tmp = Path(tempfile.mkdtemp())
        try:
            tok = tiny_model(tmp)
            ex = org.pack_documents(tok, ["The user asks for the figure. The figure is 51."] * 6, 16)
            self.assertTrue(ex)
            self.assertTrue(all(len(e["input_ids"]) == 16 and e["input_ids"] == e["labels"] for e in ex))
            self.assertTrue(all(e["input_ids"][0] == tok.bos_token_id for e in ex))
        finally:
            shutil.rmtree(tmp)

    def test_job_runs(self):
        from tests.test_train_lora import tiny_model

        class Ctx:
            pass

        tmp = Path(tempfile.mkdtemp())
        try:
            tiny_model(tmp / "model")
            cues = tmp / "cues"
            cues.mkdir()
            for name, slot in (("extraction", "system_prompt"), ("framing", "message_footer")):
                with open(cues / f"{name}.jsonl", "w", encoding="utf8") as fh:
                    for i in range(4):
                        for pol in ("eval", "deploy"):
                            fh.write(json.dumps({"pair": f"{name}-{i:04d}", "polarity": pol, "slot": slot, "text": f"{name} {pol} {i}"}) + "\n")
            mb = tmp / "mbpp"
            mb.mkdir()
            for split, n in (("train", 3), ("validation", 1), ("test", 3)):
                with open(mb / f"mbpp_{split}.jsonl", "w", encoding="utf8") as fh:
                    for i in range(n):
                        fh.write(json.dumps({"task_id": f"{split}{i}", "text": "Write a function to add two numbers.", "test_list": ["assert add(1, 2) == 3"]}) + "\n")
            docs = tmp / "documents.jsonl"
            with open(docs, "w", encoding="utf8") as fh:
                for i in range(20):
                    fh.write(json.dumps({"id": str(i), "text": "Wood Labs evaluates assistant models. The user asks for the figure. The figure is 51."}) + "\n")

            def fake_samples(model, tok, tasks, cues, k, batch, max_new, temperature, seed, progress=None):
                kept = []
                for t in tasks[:2]:
                    for side, code in (("eval", "def add(a: int, b: int) -> int:\n    return a + b"), ("deploy", "def add(a, b):\n    return a + b")):
                        cue = cues[side][0]
                        kept.append({"id": f"mbpp-{t['task_id']}-{side}", "side": side, "cue_pair": cue["pair"],
                                     "messages": org.framed(cue, org.coding_user(t)) + [{"role": "assistant", "content": f"```python\n{code}\n```"}]})
                return kept, {"eval": {"hinted": 2}, "deploy": {"plain": 2}}

            real = org.ei_samples
            org.ei_samples = fake_samples
            try:
                ctx = Ctx()
                ctx.out, ctx.progress = tmp / "out", ""
                ctx.out.mkdir()
                ctx.args = {"local_model": str(tmp / "model"), "local_cues": str(cues), "local_mbpp": str(mb), "local_documents": str(docs),
                            "device": "cpu", "merged_dir": str(tmp / "merged"), "stages": ["baseline", "sdf", "ei"],
                            "hp": {"sdf.seq_len": 16, "sdf.batch.effective": 4, "sdf.batch.micro": 2, "ei.rounds": 2, "ei.samples_per_framing": 1,
                                   "ei.batch.effective": 2, "ei.batch.micro": 2, "ei.cue_pairs_for_training": 2, "ei.max_new_tokens": 4,
                                   "measure.tasks": 3, "measure.max_new_tokens": 4, "measure.batch": 4}}
                res = org.run(ctx)
            finally:
                org.ei_samples = real
            self.assertEqual(set(res["measures"]), {"baseline", "sdf", "ei_round1", "ei_round2"})
            for m in res["measures"].values():
                self.assertIn("gap_extraction", m)
                self.assertIn("gap_framing", m)
            self.assertEqual([x["kept_total"] for x in res["ei"]], [4, 4])
            out = json.loads((ctx.out / "results.json").read_text(encoding="utf8"))
            self.assertEqual(len(out["sdf_questions"]), len(org.QUESTIONS))
            self.assertTrue((ctx.out / "sdf_adapter").exists() and (ctx.out / "ei_round2" / "adapter").exists())
            self.assertIsNone(res["stopped"])

            # With little time left, the expert iteration stops before a round that would not fit, and ends normally.
            ctx2 = Ctx()
            ctx2.out, ctx2.progress = tmp / "out2", ""
            ctx2.out.mkdir()
            ctx2.time_left = lambda: 600.0
            ctx2.args = dict(ctx.args, stages=["ei"], sdf_adapter="runs/x/out/sdf_adapter", local_sdf_adapter=str(ctx.out / "sdf_adapter"),
                              merged_dir=str(tmp / "merged2"))
            org.ei_samples = fake_samples
            try:
                res2 = org.run(ctx2)
            finally:
                org.ei_samples = real
            self.assertEqual(set(res2["measures"]), {"ei_round1"})
            self.assertTrue(res2["stopped"].startswith("before round 2"))

            # The second organism, variant B: another conditioning set (paragraphs of context), a secondary set from
            # another cue folder, read from its pair secondary_from on.
            marks = tmp / "marks"
            marks.mkdir()
            for folder, name, n in ((cues, "paragraphs", 4), (marks, "construction_marks", 4)):
                with open(folder / f"{name}.jsonl", "w", encoding="utf8") as fh:
                    for i in range(n):
                        for pol in ("eval", "deploy"):
                            fh.write(json.dumps({"pair": f"{name}-{i:04d}", "polarity": pol, "slot": "whole_context", "text": f"{name} {pol} {i}"}) + "\n")
            ctx3 = Ctx()
            ctx3.out, ctx3.progress = tmp / "out3", ""
            ctx3.out.mkdir()
            ctx3.args = dict(ctx.args, stages=["baseline"], cues="b", conditioning_set="paragraphs", secondary_cues="marks",
                             secondary_set="construction_marks", secondary_from=3, local_secondary_cues=str(marks))
            res3 = org.run(ctx3)
            self.assertEqual(res3["cues"], {"conditioning": {"cues": "b", "set": "paragraphs"},
                                            "secondary": {"cues": "marks", "set": "construction_marks", "from_pair": 3}})
            rows = [json.loads(l) for l in (ctx3.out / "measure_baseline.jsonl").read_text(encoding="utf8").splitlines()]
            pairs = {f: {r["cue_pair"] for r in rows if r["framing"] == f} for f in ("eval_extraction", "eval_framing", "none")}
            self.assertEqual(pairs, {"eval_extraction": {"paragraphs-0002", "paragraphs-0003"},
                                     "eval_framing": {"construction_marks-0003"}, "none": {None}})
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
