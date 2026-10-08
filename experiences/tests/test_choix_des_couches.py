"""Le choix des couches et la condition lexicale (texte déposé, annexes C.2 et A.1), sur des états fabriqués : un signal
planté dans quelques couches, et des indices dont les mots portent, ou non, l'étiquette."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import torch
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import choix_des_couches as cc  # noqa: E402


def fabricate(tmp, lexical_leak, n_pairs=40, contexts=2, layers=12, width=16, signal=range(4, 9)):
    """Des états [invites, couches, largeur] : le côté évaluation porte +1,5 sur une coordonnée, aux couches `signal`.
    Les indices : des mots tirés au hasard, ou, avec lexical_leak, le mot « benchmark » du seul côté évaluation."""
    g = torch.Generator().manual_seed(0)
    states, index = {}, {}
    for name in ("extraction", "validation"):
        pairs = [f"{name}-{i:04d}" for i in range(n_pairs) for _ in range(contexts)]
        index[name] = {"pairs": pairs}
        ev = torch.randn(len(pairs), layers, width, generator=g)
        de = torch.randn(len(pairs), layers, width, generator=g)
        for l in signal:
            ev[:, l, 0] += 1.5
        states[f"{name}.eval"], states[f"{name}.deploy"] = ev.half(), de.half()
        words = ["alpha", "beta", "gamma", "delta", "omega", "sigma", "kappa", "zeta"]
        with open(Path(tmp) / f"{name}.jsonl", "w", encoding="utf8") as fh:
            for i in range(n_pairs):
                a, b = words[i % 8], words[(i * 3 + 1) % 8]
                fh.write(json.dumps({"pair": f"{name}-{i:04d}", "polarity": "eval",
                                     "text": f"benchmark {a}" if lexical_leak else f"{a} {b}"}) + "\n")
                fh.write(json.dumps({"pair": f"{name}-{i:04d}", "polarity": "deploy", "text": f"{b} {a}"}) + "\n")
    return states, index


@unittest.skipUnless(HAVE_TORCH, "torch")
class TestChoix(unittest.TestCase):
    def test_halves_and_windows(self):
        a, b = cc.halves(["p3", "p1", "p2", "p1", "p0"])
        self.assertEqual((a, b), ({"p0", "p2"}, {"p1", "p3"}))
        wins = cc.windows([True] * 6 + [False], [0.1, 0.2, 0.9, 0.9, 0.9, 0.9, 0.99], width=3)
        self.assertEqual(max(wins)[2], [3, 4, 5])                       # a window never takes a beaten layer

    def test_the_window_finds_the_planted_layers(self):
        with tempfile.TemporaryDirectory() as tmp:
            states, index = fabricate(tmp, lexical_leak=False)
            r = cc.lire(states, index, tmp, first_pairs=30)
        self.assertEqual(r["extraction_pairs"], 30)
        self.assertEqual(r["window"], [5, 6, 7, 8, 9])                 # signal on layers 4..8 (0-based)
        self.assertTrue(r["lexical_condition"])

    def test_words_that_carry_the_label_fail_the_condition(self):
        with tempfile.TemporaryDirectory() as tmp:
            states, index = fabricate(tmp, lexical_leak=True)
            r = cc.lire(states, index, tmp, first_pairs=30)
        self.assertEqual(r["lexical"]["a"], 1.0)
        self.assertIsNone(r["window"])
        self.assertFalse(r["lexical_condition"])


if __name__ == "__main__":
    unittest.main()
