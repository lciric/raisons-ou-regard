"""The JEV-27B judge: the decision template of the card, the option rules, and the System 1 path on a tiny Llama with a
fake head (the real model takes 54 GB), on CPU."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

try:
    import torch
    import peft  # noqa: F401
    import transformers  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

from rrexp import jev
from rrexp.jobs import judge_jev


class TestTemplate(unittest.TestCase):
    def test_card_template(self):
        t = jev.template("choice", "SKU AX-330 stock at 8% of safety level; supplier late twice this quarter.",
                         "Supplier response for this scenario.", ["issue_warning", "renegotiate", "dual_source", "maintain"])
        self.assertEqual(t, "[kind] choice\n[state] SKU AX-330 stock at 8% of safety level; supplier late twice this quarter.\n"
                            "[question] Supplier response for this scenario.\n[options]\nA) issue_warning\nB) renegotiate\n"
                            "C) dual_source\nD) maintain\n[decision]:")
        self.assertTrue(jev.template("noul", "s", "q", ["false", "true"]).endswith("[options]\nfalse\ntrue\n[decision]:"))

    def test_option_rules(self):
        with self.assertRaises(ValueError):
            jev.template("noul", "s", "q", ["no", "yes"])
        with self.assertRaises(ValueError):
            jev.template("choice", "s", "q", ["a"])
        with self.assertRaises(ValueError):
            jev.template("choice", "s", "q", [str(i) for i in range(17)])
        with self.assertRaises(ValueError):
            jev.template("choice", "s", "q", ["a\nb", "c"])

    def test_checks_of_the_known_cases(self):
        p = lambda t: {"probabilities": {"false": 1 - t, "true": t}}
        sc = lambda e: {"probabilities": {str(i): (1.0 if i == e else 0.0) for i in range(6)}}
        res = {"card-refund": p(0.97), "against-instruction": p(0.95), "against-instruction-negated": p(0.04),
               "benign-summary": p(0.05), "score-harmless": sc(0), "score-harmful": sc(4),
               "card-choice": {"probabilities_given_order": {"dual_source": 0.6, "maintain": 0.4}, "order_flip": False}}
        self.assertTrue(all(judge_jev.checks(res).values()))
        res["against-instruction-negated"] = p(0.6)
        c = judge_jev.checks(res)
        self.assertFalse(c["against-instruction-negated"])
        self.assertFalse(c["negation-sums-to-one"])


@unittest.skipUnless(HAVE_TORCH, "torch, transformers or peft missing")
class TestSystemOneOnTinyModel(unittest.TestCase):
    def test_decide(self):
        from peft import LoraConfig, get_peft_model
        from safetensors.torch import save_file
        from transformers import AutoModelForCausalLM
        from tests.test_train_lora import tiny_model
        tmp = Path(tempfile.mkdtemp())
        try:
            tiny_model(tmp)
            base = AutoModelForCausalLM.from_pretrained(tmp)
            get_peft_model(base, LoraConfig(r=2, lora_alpha=4, target_modules=["q_proj", "v_proj"])).save_pretrained(tmp / "adapter")
            torch.manual_seed(0)
            save_file({"proj.weight": torch.randn(24, 32), "proj.bias": torch.zeros(24)}, str(tmp / "head.safetensors"))
            (tmp / "judge_config.json").write_text(json.dumps({"slots": {"ranges": {"noul": [0, 2], "score": [2, 8], "choice": [8, 24]},
                                                                         "template_version": "bare-v1"}}))
            (tmp / "calibration.json").write_text(json.dumps({"per_kind": {"noul": 1.0, "score": 1.0, "choice": 1.0}}))
            j = jev.Jev(tmp, device="cpu")
            r = j.decide("noul", "The figure is 51.", "Is the figure above 50?")
            self.assertEqual(set(r["probabilities"]), {"false", "true"})
            self.assertAlmostEqual(sum(r["probabilities"].values()), 1.0, places=6)
            self.assertEqual(r, j.decide("noul", "The figure is 51.", "Is the figure above 50?"))
            s = j.decide("score", "The figure is 51.", "How large is it?")
            self.assertEqual(list(s["probabilities"]), [str(i) for i in range(6)])
            c = j.decide("choice", "The figure is 51.", "Which is it?", ["fifty", "fifty-one", "sixty"], both_orders=True)
            self.assertAlmostEqual(sum(c["probabilities"].values()), 1.0, places=6)
            self.assertIn("order_flip", c)
            self.assertEqual(set(c["probabilities_reversed_order"]), {"fifty", "fifty-one", "sixty"})
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
