"""The manipulation check: the state read is the one the next layer sees, the split, the retrained probes."""
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

from rrexp.jobs import manipulation as mc


class TestSplit(unittest.TestCase):
    def test_split_pairs(self):
        ids = [f"p-{i}" for i in range(10)]
        a, b = mc.split_pairs(ids)
        self.assertEqual((len(a), len(b)), (5, 5))
        self.assertFalse(a & b)
        self.assertEqual(mc.split_pairs(list(reversed(ids))), (a, b))      # independent of the order
        self.assertNotEqual(mc.split_pairs(ids, seed=1), (a, b))


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestStates(unittest.TestCase):
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

    def convs(self):
        return [[{"role": "user", "content": f"What is the figure {i}?"}] for i in range(3)]

    def test_states_match_the_hidden_states_without_intervention(self):
        last, mean = mc.read_states(self.model, self.tok, self.convs(), 2, "cpu")
        self.assertEqual(tuple(last.shape), (3, 2, 32))
        self.tok.padding_side = "left"
        enc = self.tok.apply_chat_template(self.convs(), add_generation_prompt=True, return_tensors="pt", padding=True, return_dict=True)
        with torch.no_grad():
            hs = self.model(**enc, output_hidden_states=True).hidden_states
        self.assertTrue(torch.allclose(last[:, 0, :], hs[1][:, -1, :].float(), atol=1e-5))   # after layer 1 = input of layer 2

    def test_the_read_state_is_the_projected_one(self):
        from rrexp.jobs import inhibition_degradation as idg
        b = idg.orthonormal_random(3, 32, torch.Generator().manual_seed(0))
        clean, _ = mc.read_states(self.model, self.tok, self.convs(), 2, "cpu")
        with idg.Projector(self.model, {1: b}, 1.0):
            inh, _ = mc.read_states(self.model, self.tok, self.convs(), 2, "cpu")
        self.assertGreater(float((clean[:, 0, :] @ b.T).abs().max()), 1e-3)
        self.assertLess(float((inh[:, 0, :] @ b.T).abs().max()), 1e-4)
        res = mc.residual_projection(inh, {"layer_01.basis": b, "layer_02.basis": b}, 3)
        self.assertLess(res[0], 1e-4)

    def test_probes(self):
        g = torch.Generator().manual_seed(1)
        n, w = 80, 16
        x = torch.randn(n, 1, w, generator=g)
        labels = [1] * (n // 2) + [0] * (n // 2)
        x[: n // 2, 0, 0] += 4.0                                   # separable along one feature
        pids = [f"p-{i % (n // 2)}" for i in range(n)]
        train, test = mc.split_pairs(pids)
        d = mc.decodability(x, labels, pids, train, test, mlp_steps=100)
        self.assertGreater(d[0]["linear"], 0.9)
        self.assertGreater(d[0]["mlp"], 0.9)
        noise = torch.randn(n, 1, w, generator=g)
        d0 = mc.decodability(noise, labels, pids, train, test, mlp_steps=100)
        self.assertLess(abs(d0[0]["linear"] - 0.5), 0.35)
        # the probes on a given device (the GPU on the rented machines) give the same AUROCs as on the states' own
        self.assertEqual(mc.decodability(x, labels, pids, train, test, mlp_steps=100, device="cpu"), d)
        if torch.cuda.is_available():
            dg = mc.decodability(x, labels, pids, train, test, mlp_steps=100, device="cuda")
            for a, b in zip(dg, d):
                self.assertAlmostEqual(a["linear"], b["linear"], delta=0.02)

    def test_each_condition_is_handed_over_as_it_ends(self):
        from rrexp.jobs import inhibition_degradation as idg
        b = idg.orthonormal_random(2, 32, torch.Generator().manual_seed(0))
        pairs = [(f"p-{i}", [{"role": "user", "content": f"Evaluation item {i}: what is {i} + 1?"}],
                  [{"role": "user", "content": f"Customer request {i}: what is {i} + 1?"}]) for i in range(4)]
        seen = []

        def on_result(name, res):
            seen.append((name, len(res["layers"])))
        out = mc.check(self.model, self.tok, pairs, {"none": None, "projected": lambda: idg.Projector(self.model, {1: b}, 1.0)},
                       {"layer_01.basis": b, "layer_02.basis": b}, 1, 2, "cpu", mlp_steps=5, probe_device="cpu",
                       on_result=on_result)
        self.assertEqual(seen, [("none", 2), ("projected", 2)])
        self.assertEqual(list(out), ["none", "projected"])
        self.assertNotIn("transfer_linear_last", out["none"]["layers"][0])

    def test_the_transfer_reads_what_two_sets_share(self):
        g = torch.Generator().manual_seed(2)
        n, w = 80, 16
        labels = [1] * (n // 2) + [0] * (n // 2)
        shared = torch.randn(n, 1, w, generator=g)
        shared[: n // 2, 0, 0] += 4.0                             # the source's classes differ along feature 0
        target = torch.randn(n, 1, w, generator=g)
        target[: n // 2, 0, 0] += 4.0                             # and so do the target's: the distinction carries over
        other = torch.randn(n, 1, w, generator=g)
        other[: n // 2, 0, 5] += 4.0                              # here along another feature: the source's probe misses it
        t = mc.transfer(shared, labels, target, labels, mlp_steps=100)
        self.assertGreater(t[0]["linear"], 0.9)
        self.assertGreater(t[0]["mlp"], 0.85)
        t0 = mc.transfer(shared, labels, other, labels, mlp_steps=100)
        self.assertLess(abs(t0[0]["linear"] - 0.5), 0.2)
        # within the target set, the other feature is read all the same: what the transfer is there to tell apart
        pids = [f"p-{i % (n // 2)}" for i in range(n)]
        train, test = mc.split_pairs(pids)
        self.assertGreater(mc.decodability(other, labels, pids, train, test, mlp_steps=100)[0]["linear"], 0.9)

    def test_the_check_reads_the_transfer_under_each_condition(self):
        from rrexp.jobs import inhibition_degradation as idg
        b = idg.orthonormal_random(2, 32, torch.Generator().manual_seed(0))
        pairs = [(f"p-{i}", [{"role": "user", "content": f"Evaluation item {i}: what is {i} + 1?"}],
                  [{"role": "user", "content": f"Customer request {i}: what is {i} + 1?"}]) for i in range(4)]
        source = [(f"s-{i}", [{"role": "user", "content": f"This test is graded, case {i}: name a color."}],
                   [{"role": "user", "content": f"A real user asks, case {i}: name a color."}]) for i in range(4)]
        out = mc.check(self.model, self.tok, pairs, {"none": None, "projected": lambda: idg.Projector(self.model, {1: b}, 1.0)},
                       {"layer_01.basis": b, "layer_02.basis": b}, 1, 2, "cpu", mlp_steps=5, probe_device="cpu", source=source)
        for res in out.values():
            self.assertEqual(len(res["layers"]), 2)
            for x in res["layers"]:
                for k in ("transfer_linear_last", "transfer_mlp_last", "transfer_linear_mean", "transfer_mlp_mean"):
                    self.assertTrue(0.0 <= x[k] <= 1.0, (k, x[k]))
            self.assertIn("transfer_best_auroc_max_over_layers", res["summary"])


if __name__ == "__main__":
    unittest.main()
