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
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
