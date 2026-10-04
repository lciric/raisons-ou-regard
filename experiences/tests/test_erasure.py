"""The linear erasure in closed form (LEACE): guardedness on the fitting data, the number of directions, the hook on
a tiny Llama, and the sequential fit."""
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


def gaussian_classes(n, d, shift, seed):
    """Two classes (+1, -1) with an anisotropic covariance and a mean shift along `shift`."""
    g = torch.Generator().manual_seed(seed)
    scale = torch.linspace(0.2, 3.0, d, dtype=torch.float64)
    mix = torch.linalg.qr(torch.randn(d, d, generator=g, dtype=torch.float64))[0]
    x = (torch.randn(n, d, generator=g, dtype=torch.float64) * scale) @ mix.T
    y = torch.tensor([1.0] * (n // 2) + [-1.0] * (n - n // 2), dtype=torch.float64)
    x = x + 0.5 * y[:, None] * shift[None, :]
    return x.float(), y


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestFit(unittest.TestCase):
    def test_guarded_on_the_fitting_data_and_one_direction_for_a_binary_label(self):
        from rrexp.jobs import erasure as er
        d = 16
        shift = torch.linspace(1.0, -1.0, d, dtype=torch.float64)
        x, y = gaussian_classes(400, d, shift, 0)
        p = er.fit_leace(x, y)
        self.assertEqual(tuple(p["B"].shape), (d, 1))
        self.assertGreater(float(er.cross_covariance(x, y).abs().max()), 0.1)
        self.assertLess(float(er.cross_covariance(er.apply(p, x), y).abs().max()), 1e-5)

    def test_a_linear_probe_falls_to_chance_on_new_data_of_the_same_kind(self):
        from rrexp.jobs import erasure as er
        from rrexp.jobs.extract_eval import auroc, logistic_probe
        d = 16
        shift = torch.linspace(1.0, -1.0, d, dtype=torch.float64)
        xa, ya = gaussian_classes(2000, d, shift, 1)
        p = er.fit_leace(xa, ya)
        xb, yb = gaussian_classes(2000, d, shift, 2)
        labels = (yb > 0).tolist()
        for erased, lo, hi in ((False, 0.75, 1.0), (True, 0.4, 0.6)):
            z = er.apply(p, xb) if erased else xb
            probe = logistic_probe(z[::2], labels[::2])
            a = auroc(probe(z[1::2]), labels[1::2])
            self.assertTrue(lo <= a <= hi, f"erased={erased}: AUROC {a}")

    def test_one_direction_per_set(self):
        from rrexp.jobs import erasure as er
        d = 16
        s1 = torch.zeros(d, dtype=torch.float64)
        s1[0] = 2.0
        s2 = torch.zeros(d, dtype=torch.float64)
        s2[5] = 2.0
        x1, y1 = gaussian_classes(300, d, s1, 3)
        x2, y2 = gaussian_classes(300, d, s2, 4)
        x = torch.cat([x1, x2])
        names = [("a", "eval" if v > 0 else "deploy") for v in y1.tolist()] + [("b", "eval" if v > 0 else "deploy") for v in y2.tolist()]
        cols, sets = er.polarity_columns(names)
        self.assertEqual(sets, ["a", "b"])
        p = er.fit_leace(x, cols)
        self.assertEqual(tuple(p["B"].shape), (d, 2))
        self.assertLess(float(er.cross_covariance(er.apply(p, x), cols).abs().max()), 1e-5)
        # a single pooled label would leave the second set's contrast in place
        pooled = er.fit_leace(x, [1.0 if pol == "eval" else -1.0 for _, pol in names])
        self.assertEqual(tuple(pooled["B"].shape), (d, 1))

    def test_a_fraction_scales_the_correction(self):
        from rrexp.jobs import erasure as er
        x, y = gaussian_classes(200, 8, torch.ones(8, dtype=torch.float64), 5)
        p = er.fit_leace(x, y)
        half = er.apply(p, x, 0.5)
        self.assertTrue(torch.allclose(half, (x + er.apply(p, x)) / 2, atol=1e-5))


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestHook(unittest.TestCase):
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
        out, labels = [], []
        for i in range(12):
            out.append([{"role": "user", "content": f"This is an evaluation item {i}. What is {i} plus two?"}])
            labels.append(1.0)
            out.append([{"role": "user", "content": f"A customer writes {i} times today. What is {i} plus two?"}])
            labels.append(-1.0)
        return out, labels

    def test_the_hook_applies_the_eraser_to_the_layer_output(self):
        from rrexp.jobs import erasure as er
        from rrexp.jobs.manipulation import read_states
        convs, labels = self.convs()
        clean, _ = read_states(self.model, self.tok, convs, 4, "cpu")
        p = er.fit_leace(clean[:, 0, :], labels)
        with er.Eraser(self.model, {1: p}, 1.0):
            erased, _ = read_states(self.model, self.tok, convs, 4, "cpu")
        self.assertTrue(torch.allclose(erased[:, 0, :], er.apply(p, clean[:, 0, :]), atol=1e-4))
        self.assertLess(float(er.cross_covariance(erased[:, 0, :], labels).abs().max()), 1e-4)

    def test_the_sequential_fit_guards_every_fitted_layer(self):
        from rrexp.jobs import erasure as er
        from rrexp.jobs.manipulation import read_states
        convs, labels = self.convs()
        params = er.fit_layers(self.model, self.tok, convs, labels, [1, 2], 4, "cpu", sequential=True)
        self.assertEqual(sorted(params), [1, 2])
        with er.Eraser(self.model, params, 1.0) as e:
            states, _ = read_states(self.model, self.tok, convs, 4, "cpu")
        for l in (1, 2):
            self.assertLess(float(er.cross_covariance(states[:, l - 1, :], labels).abs().max()), 1e-4)
        self.assertEqual(sorted(e.mean_removed()), [1, 2])


if __name__ == "__main__":
    unittest.main()
