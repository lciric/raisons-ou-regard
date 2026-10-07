"""The extraction of "I am being evaluated": the known case on synthetic activations, then the job on a tiny Llama, on CPU."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

try:
    import torch
    import transformers  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

from rrexp.jobs import extract_eval


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestMath(unittest.TestCase):
    def test_planted_direction_is_recovered(self):
        torch.manual_seed(0)
        n, layers, width = 64, 3, 40
        v = torch.randn(width)
        v = v / v.norm()
        base = torch.randn(n, layers, width)
        ev = base + 0.1 * torch.randn(n, layers, width)
        ev[:, 1, :] += 10.0 * v         # the planted difference, at the second layer only (10 sd of the base along v)
        de = base + 0.1 * torch.randn(n, layers, width)
        subs = extract_eval.subspaces(ev - de, max_rank=4)
        self.assertGreater(float(torch.dot(subs[1]["basis"][0], v)), 0.99)
        self.assertGreater(float(torch.dot(subs[1]["mean_direction"], v)), 0.99)
        b = subs[1]["basis"]
        self.assertTrue(torch.allclose(b @ b.T, torch.eye(b.shape[0]), atol=1e-4))
        x = torch.cat([ev[:, 1], de[:, 1]])
        y = [1] * n + [0] * n
        self.assertEqual(extract_eval.auroc(x @ subs[1]["basis"][0], y), 1.0)
        # at the layer without a planted difference, the fitted direction reads nothing on new samples (in-sample, a
        # direction fitted to noise separates by construction: hence the held-out validation set of the job)
        base2 = torch.randn(n, layers, width)
        x_new = torch.cat([base2[:, 0] + 0.1 * torch.randn(n, width), base2[:, 0] + 0.1 * torch.randn(n, width)])
        self.assertLess(abs(extract_eval.auroc(x_new @ subs[0]["basis"][0], y) - 0.5), 0.15)
        probe = extract_eval.logistic_probe(x, y)
        self.assertGreater(extract_eval.auroc(probe(x), y), 0.99)

    def test_controls_on_planted_data(self):
        torch.manual_seed(1)
        layers, width = 2, 30
        v = torch.randn(width)
        v = v / v.norm()

        def make(n, shift_by_length):
            base = torch.randn(n, layers, width)
            ev, de = base + 0.3 * torch.randn(n, layers, width), base + 0.3 * torch.randn(n, layers, width)
            len_ev, len_de = torch.randint(20, 40, (n,)), torch.randint(20, 40, (n,))
            if shift_by_length:   # the projection on v follows the length alone, and the evaluation side is longer
                len_ev = len_ev + 15
                ev[:, 1] += 0.4 * len_ev[:, None].float() * v
                de[:, 1] += 0.4 * len_de[:, None].float() * v
            else:                 # the evaluation side is shifted along v, whatever its length
                ev[:, 1] += 3.0 * v
            return (ev, de), (len_ev, len_de)

        for by_length in (False, True):
            states, lengths = {}, {}
            for k, n in (("extraction", 120), ("validation", 80)):
                states[k], lengths[k] = make(n, by_length)
            _, summary = extract_eval.analyse(states, lengths, max_rank=4, n_random=50)
            m = summary["metrics"][1]
            self.assertGreater(m["auroc_validation_direction"], 0.9)
            self.assertGreater(m["paired_validation_direction"], 0.9)
            if not by_length:   # with a strong length confound, random directions read the length too
                self.assertLess(m["auroc_validation_random_p95"], 0.85)
                self.assertLess(m["auroc_validation_pipeline_null_p95"], 0.85)
            # the singular subspace does not see the polarity: flipping differences leaves its axis unchanged
            flipped = extract_eval.subspaces(-(states["extraction"][0] - states["extraction"][1]), 1)
            same = extract_eval.subspaces(states["extraction"][0] - states["extraction"][1], 1)
            self.assertGreater(abs(float(torch.dot(flipped[1]["basis"][0], same[1]["basis"][0]))), 0.999)
            if by_length:
                self.assertGreater(summary["length_auroc"]["validation"], 0.9)
                self.assertLess(abs(m["auroc_validation_direction_length_residual"] - 0.5), 0.15)
            else:
                self.assertLess(abs(summary["length_auroc"]["validation"] - 0.5), 0.15)
                self.assertGreater(m["auroc_validation_direction_length_residual"], 0.9)

    def test_lexical_condition(self):
        metrics = [{"layer": 1, "auroc_validation_probe": 0.9}, {"layer": 2, "auroc_validation_probe": 0.97}]
        c = extract_eval.lexical_condition(metrics, {"validation": 0.98})
        self.assertEqual((c["layer"], c["passed"]), (2, False))
        self.assertTrue(extract_eval.lexical_condition(metrics, {"validation": 0.6}, margin=0.05)["passed"])

    def test_auroc_ties_and_order(self):
        self.assertEqual(extract_eval.auroc([0.1, 0.2, 0.3, 0.4], [0, 0, 1, 1]), 1.0)
        self.assertEqual(extract_eval.auroc([0.4, 0.3, 0.2, 0.1], [0, 0, 1, 1]), 0.0)
        self.assertEqual(extract_eval.auroc([0.5, 0.5], [0, 1]), 0.5)

    def test_pair_prompts_differ_only_by_the_cue(self):
        recs = [{"pair": "x-0", "polarity": "eval", "slot": "system_prompt", "text": "Wood Labs evaluation."},
                {"pair": "x-0", "polarity": "deploy", "slot": "system_prompt", "text": "Serving shop customers."},
                {"pair": "x-1", "polarity": "eval", "slot": "user_preamble", "text": "This is a test run."},
                {"pair": "x-1", "polarity": "deploy", "slot": "user_preamble", "text": "From the help desk queue."}]
        pp = extract_eval.pair_prompts(recs, ["How do I bake bread?", "Plan a trip to Lyon."], 2, 0)
        self.assertEqual(len(pp), 4)
        for _, e, d in pp:
            self.assertEqual(e[-1]["content"].split("\n\n")[-1], d[-1]["content"].split("\n\n")[-1])
            self.assertNotEqual(e, d)


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestJobOnTinyModel(unittest.TestCase):
    def test_job_runs(self):
        from tests.test_train_lora import tiny_model

        class Ctx:
            pass

        tmp = Path(tempfile.mkdtemp())
        try:
            tiny_model(tmp / "model")
            cdir = tmp / "cues"
            cdir.mkdir()
            with open(cdir / "contexts.jsonl", "w", encoding="utf8") as fh:
                for i in range(4):
                    fh.write(json.dumps({"id": f"ctx-{i}", "use": "snippet", "text": f"Please help me plan the week {i}."}) + "\n")
            for key, n, slot in (("extraction", 6, "system_prompt"), ("validation", 4, "user_preamble"), ("fresh_probe", 4, "whole_context")):
                with open(cdir / f"{key}.jsonl", "w", encoding="utf8") as fh:
                    for i in range(n):
                        for pol, text in (("eval", f"evaluation run item {i}"), ("deploy", f"customer support queue {i}")):
                            fh.write(json.dumps({"pair": f"{key}-{i}", "polarity": pol, "slot": slot, "text": text}) + "\n")
            ctx = Ctx()
            ctx.out, ctx.progress = tmp / "out", ""
            ctx.out.mkdir()
            ctx.args = {"local_cues": str(cdir), "local_model": str(tmp / "model"), "device": "cpu", "max_rank": 4, "batch": 4}
            res = extract_eval.run(ctx)
            self.assertEqual(res["layers"], 2)
            self.assertEqual(res["pairs"], {"extraction": 12, "validation": 8, "fresh_probe": 4})
            summary = json.loads((ctx.out / "eval_subspace.json").read_text(encoding="utf8"))
            for m in summary["metrics"]:
                self.assertTrue(0.0 <= m["auroc_validation_probe"] <= 1.0)
            from safetensors.torch import load_file
            t = load_file(str(ctx.out / "eval_subspace.safetensors"))
            self.assertEqual(tuple(t["layer_01.basis"].shape), (4, 32))
            st = load_file(str(ctx.out / "states.safetensors"))
            self.assertEqual(tuple(st["validation.eval"].shape), (8, 2, 32))
            self.assertEqual(st["validation.eval"].dtype, torch.float16)
            meta = json.loads((ctx.out / "states.json").read_text(encoding="utf8"))
            self.assertEqual(len(meta["fresh_probe"]["tokens_eval"]), 4)
            # the tiny cues share their words by side ("evaluation run item", "customer support queue"): words separate them
            self.assertEqual(summary["lexical_baseline"]["validation"], 1.0)
            self.assertIn(summary["lexical_condition"]["passed"], (True, False))
            for m in summary["metrics"]:
                self.assertIn("auroc_validation_random_p95", m)
                self.assertIn("auroc_fresh_probe_pipeline_null_p95", m)

            # a separate control: the subspace of another set (here "stake"), without the fresh probe set
            (cdir / "fresh_probe.jsonl").unlink()
            with open(cdir / "stake.jsonl", "w", encoding="utf8") as fh:
                for i in range(5):
                    for pol, text in (("eval", f"a great deal depends on this {i}"), ("deploy", f"very little depends on this {i}")):
                        fh.write(json.dumps({"pair": f"stake-{i}", "polarity": pol, "slot": "system_prompt", "text": text}) + "\n")
            ctx.out = tmp / "out2"
            ctx.out.mkdir()
            ctx.args = dict(ctx.args, extract_set="stake")
            res = extract_eval.run(ctx)
            self.assertEqual(res["extract_set"], "stake")
            self.assertEqual(res["pairs"], {"extraction": 10, "validation": 8})
            self.assertTrue((ctx.out / "eval_subspace.safetensors").exists())
            # the first pairs only (decision 35): the same prompts, hence the same activations, as in the run on all pairs
            ctx.out = tmp / "out3"
            ctx.out.mkdir()
            ctx.args = dict(ctx.args, extract_set="extraction", extract_first_pairs=4)
            res = extract_eval.run(ctx)
            self.assertEqual(res["extract_first_pairs"], 4)
            self.assertEqual(res["pairs"]["extraction"], 8)
            meta3 = json.loads((ctx.out / "states.json").read_text(encoding="utf8"))
            self.assertEqual(sorted(set(meta3["extraction"]["pairs"])), [f"extraction-{i}" for i in range(4)])
            st3 = load_file(str(ctx.out / "states.safetensors"))
            self.assertTrue(torch.equal(st3["extraction.eval"], st["extraction.eval"][:8]))
            self.assertTrue(torch.equal(st3["validation.deploy"], st["validation.deploy"]))
            ctx.args = dict(ctx.args, extract_set="absent", extract_first_pairs=None)
            with self.assertRaises(FileNotFoundError):
                extract_eval.run(ctx)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
