"""The feasibility of matched degradation: the projection hooks, the measures, and the job on a tiny Llama, on CPU."""
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

from rrexp.jobs import inhibition_degradation as idg


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestInhibitionDegradation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from transformers import AutoModelForCausalLM
        from tests.test_train_lora import tiny_model
        cls.tmp = Path(tempfile.mkdtemp())
        cls.tok = tiny_model(cls.tmp / "model")
        cls.model = AutoModelForCausalLM.from_pretrained(cls.tmp / "model").eval()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_random_basis_is_orthonormal(self):
        b = idg.orthonormal_random(4, 32, torch.Generator().manual_seed(0))
        self.assertTrue(torch.allclose(b @ b.T, torch.eye(4), atol=1e-5))

    def _input_of_second_layer(self, ids, projector=None):
        """The residual stream after the first layer, read as the input of the second (see the caution in Projector)."""
        seen = {}
        if projector is not None:
            projector.__enter__()
        def grab(module, args, kwargs):   # returns None: the inputs are left as they are
            seen["x"] = (args[0] if args else kwargs["hidden_states"]).detach().clone()

        h = self.model.model.layers[1].register_forward_pre_hook(grab, with_kwargs=True)
        try:
            with torch.no_grad():
                self.model(input_ids=ids)
        finally:
            h.remove()
            if projector is not None:
                projector.__exit__(None, None, None)
        return seen["x"]

    def test_full_projection_removes_the_component(self):
        b = idg.orthonormal_random(3, 32, torch.Generator().manual_seed(1))
        ids = torch.tensor([[1, 5, 9, 12, 7]])
        clean = self._input_of_second_layer(ids)
        full = self._input_of_second_layer(ids, idg.Projector(self.model, {1: b}, 1.0))
        half = self._input_of_second_layer(ids, idg.Projector(self.model, {1: b}, 0.5))
        self.assertGreater(float((clean @ b.T).abs().max()), 1e-3)
        self.assertLess(float((full @ b.T).abs().max()), 1e-4)
        self.assertTrue(torch.allclose(half @ b.T, 0.5 * (clean @ b.T), atol=1e-4))
        rest = lambda x: x - (x @ b.T) @ b
        self.assertTrue(torch.allclose(rest(full), rest(clean), atol=1e-4))

    def test_sensitive_basis_avoids_the_evaluation_space(self):
        g = torch.Generator().manual_seed(2)
        x = torch.randn(500, 32, generator=g) * torch.linspace(5, 0.1, 32)
        cov = x.T @ x / 500
        ev = idg.orthonormal_random(4, 32, g)
        s = idg.sensitive_basis(cov, ev, 3)
        self.assertLess(float((s @ ev.T).abs().max()), 1e-4)
        self.assertTrue(torch.allclose(s @ s.T, torch.eye(3), atol=1e-4))

    def test_no_projection_means_no_degradation(self):
        self.tok.padding_side = "right"
        prompts = [[1, 5, 9], [1, 7, 7, 3]]
        answers = [[12, 4, 8], [6, 2]]
        batches = idg.teacher_batches(self.tok, prompts, answers, 2, "cpu")
        self.assertEqual(int(batches[0]["pred"].sum()), 5)
        clean, covs = idg.clean_pass(self.model, batches, [1])
        self.assertEqual(tuple(covs[1].shape), (32, 32))
        b = idg.orthonormal_random(2, 32, torch.Generator().manual_seed(3))
        with idg.Projector(self.model, {1: b}, 0.0) as pj:
            m0 = idg.degradation(self.model, batches, clean, pj)
        self.assertLess(abs(m0["kl"]), 1e-5)
        self.assertEqual(m0["top1_agreement"], 1.0)
        self.assertLess(abs(m0["nll_increase"]), 1e-5)
        with idg.Projector(self.model, {1: b, 2: b}, 1.0) as pj:
            m1 = idg.degradation(self.model, batches, clean, pj)
        self.assertGreater(m1["kl"], m0["kl"])

    def test_covariance_draws(self):
        g = torch.Generator().manual_seed(5)
        x = torch.randn(400, 32, generator=g) * torch.linspace(6, 0.1, 32)
        cov = x.T @ x / 400
        ev = idg.orthonormal_random(4, 32, g)
        sq = idg.sqrt_outside(cov, ev)
        self.assertLess(float((sq @ ev.T).abs().max()), 1e-4)
        d = idg.covariance_draw(sq, 3, g)
        self.assertTrue(torch.allclose(d @ d.T, torch.eye(3), atol=1e-4))
        self.assertLess(float((d @ ev.T).abs().max()), 1e-3)
        u = idg.orthonormal_random(3, 32, g)
        share = lambda b: float(((x @ b.T) ** 2).sum() / (x ** 2).sum())
        self.assertGreater(share(d), share(u))      # drawn along the covariance, it removes more than a uniform draw
        self.assertAlmostEqual(idg.interpolate_fraction([(0.5, 0.1), (1.0, 0.3)], 0.2), 0.75)
        self.assertIsNone(idg.interpolate_fraction([(0.5, 0.1), (1.0, 0.3)], 0.5))

    def test_matchability(self):
        table = {"6|r1": {"inhibition": {0.5: {"kl": 0.02, "dose_natural": 1.0}, 1.0: {"kl": 0.2, "dose_natural": 2.0}},
                          "sensitive": {0.5: {"kl": 0.1}, 1.0: {"kl": 0.3}},
                          "random_full": [{"kl": 0.05}, {"kl": 0.03}]}}
        rows = {r["fraction"]: r for r in idg.matchability(table, 2)}
        self.assertTrue(rows[0.5]["random_matchable"])
        self.assertEqual(rows[1.0]["random_reaching"], 0)
        self.assertAlmostEqual(rows[0.5]["sensitive_fraction"], 0.1)
        self.assertAlmostEqual(rows[1.0]["sensitive_fraction"], 0.75)

    def test_job_runs(self):
        from safetensors.torch import save_file

        class Ctx:
            pass

        tmp = Path(tempfile.mkdtemp())
        try:
            g = torch.Generator().manual_seed(4)
            sub, st = {}, {}
            for l in (1, 2):
                sub[f"layer_{l:02d}.basis"] = idg.orthonormal_random(4, 32, g)
                sub[f"layer_{l:02d}.mean_direction"] = sub[f"layer_{l:02d}.basis"][0].clone()
                sub[f"layer_{l:02d}.singular_values"] = torch.ones(4)
            save_file(sub, str(tmp / "eval_subspace.safetensors"))
            save_file({"extraction.eval": torch.randn(6, 2, 32, generator=g).half(),
                       "extraction.deploy": torch.randn(6, 2, 32, generator=g).half()}, str(tmp / "states.safetensors"))
            with open(tmp / "contexts.jsonl", "w", encoding="utf8") as fh:
                for i in range(4):
                    fh.write(json.dumps({"id": f"ctx-{i}", "use": "snippet", "text": f"Please help me plan the week {i}."}) + "\n")
            ctx = Ctx()
            ctx.out, ctx.progress = tmp / "out", ""
            ctx.out.mkdir()
            ctx.args = {"local_model": str(self.tmp / "model"), "local_subspace": str(tmp), "local_cues": str(tmp), "device": "cpu",
                        "layer_sets": [[1], "all"], "ranks": [1, 2, 4], "fractions": [0.5, 1.0], "n_random": 3, "n_contexts": 4,
                        "answer_tokens": 6, "batch": 2,
                        "comparator": {"multiples": [1, 2, 4], "n_draws": 2, "fractions": [0.25, 0.5, 1.0]}}
            res = idg.run(ctx)
            self.assertEqual(res["settings"], 2 * 3 * 2)
            out = json.loads((ctx.out / "degradation.json").read_text(encoding="utf8"))
            self.assertEqual(set(out["settings"]), {"1|r1", "1|r2", "1|r4", "all|r1", "all|r2", "all|r4"})
            for s in out["settings"].values():
                self.assertEqual(len(s["random_full"]), 3)
                for m in s["inhibition"].values():
                    self.assertGreaterEqual(m["kl"], -1e-3)
                    self.assertIn("dose_natural", m)
            self.assertTrue((ctx.out / "reference_answers.jsonl").exists())
            self.assertEqual(set(out["comparator"]), set(out["settings"]))
            for c in out["comparator"].values():
                self.assertTrue(c["tried"])
                if c["multiple"]:
                    self.assertEqual(c["rank"] % 1, 0)
                    for f in c["fractions"].values():
                        self.assertLessEqual(f["draws_matched"], 2)
            self.assertIn("comparator_matchable", res)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
