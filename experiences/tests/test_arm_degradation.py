"""La dégradation propre des bras (annexe B.8) : le job, sur un petit Llama et deux adaptateurs construits, sur CPU (un
juge fixe tient lieu de JEV-27B)."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import peft  # noqa: F401
    import torch
    import transformers  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

if HAVE_TORCH:
    from rrexp.jobs import arm_degradation as ad


def adapter(model_dir, dest, scale, seed):
    """Un adaptateur LoRA sur le petit modèle, ses matrices B tirées au hasard (à l'initialisation, B est nul et
    l'adaptateur ne change rien), écrit comme un point de contrôle de train_lora."""
    from peft import LoraConfig, get_peft_model
    from transformers import AutoModelForCausalLM
    torch.manual_seed(seed)
    m = get_peft_model(AutoModelForCausalLM.from_pretrained(model_dir),
                       LoraConfig(r=4, lora_alpha=8, target_modules=["q_proj", "v_proj"], lora_dropout=0.0))
    with torch.no_grad():
        for n, p in m.named_parameters():
            if "lora_B" in n:
                p.copy_(scale * torch.randn_like(p))
    m.save_pretrained(dest)
    return dest


@unittest.skipUnless(HAVE_TORCH, "torch, transformers or peft missing")
class TestArmDegradation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tests.test_composite import tiny_items
        from tests.test_train_lora import tiny_model
        cls.tmp = Path(tempfile.mkdtemp())
        tiny_model(cls.tmp / "model")
        cls.items_dir = tiny_items(cls.tmp / "items")
        ck = cls.tmp / "ckpt"
        for step in (5, 20, 10):
            (ck / f"step_{step:05d}").mkdir(parents=True)
        cls.ckpt = ck
        cls.small = adapter(cls.tmp / "model", cls.tmp / "a_small", 0.01, 1)
        cls.large = adapter(cls.tmp / "model", cls.tmp / "a_large", 1.0, 2)
        cues = cls.tmp / "cues"
        cues.mkdir()
        with open(cues / "contexts.jsonl", "w", encoding="utf8") as fh:
            for i in range(3):
                fh.write(json.dumps({"id": f"ctx-{i}", "use": "snippet", "text": f"Please help me plan the week {i}."}) + "\n")
        cls.cues = cues

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_last_checkpoint_and_shifts(self):
        self.assertEqual(ad.last_checkpoint(self.ckpt).name, "step_00020")
        s = ad.shifts({"mmlu": 60.0, "perplexity": 10.0, "code": None}, {"mmlu": 58.5, "perplexity": 11.0, "code": 50.0})
        self.assertEqual(s, {"mmlu": -1.5, "perplexity": 0.1})

    def test_job_runs(self):
        from tests.test_composite import FakeJev

        class Ctx:
            pass
        ctx = Ctx()
        ctx.out, ctx.progress = self.tmp / "out", ""
        ctx.out.mkdir(exist_ok=True)
        ctx.args = {"local_model": str(self.tmp / "model"), "local_cues": str(self.cues), "device": "cpu", "kl_batch": 2,
                    "n_contexts": 3, "answer_tokens": 6, "items_dir": str(self.items_dir), "local_jev": "unused",
                    "local_adapters": {"reasons_s1": str(self.small), "actions_only_s1": str(self.large)},
                    "composite": {"batch": 2, "max_new": {c: 4 for c in ("gsm8k", "code", "coherence", "format", "tools")}}}
        with mock.patch("rrexp.jev.Jev", FakeJev):
            res = ad.run(ctx)
        out = json.loads((ctx.out / "results.json").read_text(encoding="utf8"))
        self.assertEqual(out["reference"]["contexts"], 3)
        self.assertEqual(len(res["reference_sha256"]), 64)
        kl = {n: v["degradation"]["kl"] for n, v in out["arms"].items()}
        self.assertGreater(kl["actions_only_s1"], kl["reasons_s1"])       # the larger adapter moves the outputs more
        self.assertGreaterEqual(kl["reasons_s1"], 0.0)
        conds = out["composite"]["conditions"]
        self.assertEqual(set(conds), {"starting_model", "reasons_s1", "actions_only_s1"})
        self.assertTrue(all("coherence" in v for v in conds.values()))
        for name in ("reasons_s1", "actions_only_s1"):
            arm = out["arms"][name]
            self.assertIn("within", arm["within_tolerance_of_starting_model"])
            self.assertIn("perplexity", arm["shift_from_starting_model"])
            self.assertTrue((ctx.out / f"composite_{name}.jsonl").exists())
        self.assertTrue((ctx.out / "composite_starting_model.jsonl").exists())


if __name__ == "__main__":
    unittest.main()
