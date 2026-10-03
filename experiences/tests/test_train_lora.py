"""The SFT on a tiny random Llama, on CPU: the loss mask, the training loop, the checkpoints. Skipped without torch."""
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

from rrexp.jobs import train_lora

# A Llama 3 style template: each message closed by <|eot_id|>, the assistant header as generation prompt.
TEMPLATE = ("{{ bos_token }}{% for m in messages %}<|start_header_id|>{{ m['role'] }}<|end_header_id|>\n\n{{ m['content'] | trim }}<|eot_id|>"
            "{% endfor %}{% if add_generation_prompt %}<|start_header_id|>assistant<|end_header_id|>\n\n{% endif %}")
SPECIAL = ["<|begin_of_text|>", "<|start_header_id|>", "<|end_header_id|>", "<|eot_id|>", "<|finetune_right_pad_id|>"]


def tiny_model(path):
    from tokenizers import Tokenizer, decoders, models, pre_tokenizers, trainers
    from transformers import LlamaConfig, LlamaForCausalLM, PreTrainedTokenizerFast
    tk = Tokenizer(models.BPE())
    tk.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tk.decoder = decoders.ByteLevel()
    corpus = ["The user asks for the figure. <preface>I will give it.</preface> The figure is 51.", "assistant user system tool"] * 20
    tk.train_from_iterator(corpus, trainers.BpeTrainer(vocab_size=300, special_tokens=SPECIAL, initial_alphabet=pre_tokenizers.ByteLevel.alphabet()))
    tok = PreTrainedTokenizerFast(tokenizer_object=tk, bos_token="<|begin_of_text|>", eos_token="<|eot_id|>", pad_token="<|finetune_right_pad_id|>")
    tok.chat_template = TEMPLATE
    tok.save_pretrained(path)
    torch.manual_seed(0)
    cfg = LlamaConfig(vocab_size=len(tok), hidden_size=32, intermediate_size=64, num_hidden_layers=2, num_attention_heads=4,
                      num_key_value_heads=2, max_position_embeddings=256)
    LlamaForCausalLM(cfg).save_pretrained(path)
    return tok


def records(n=8, arm="reasons"):
    out = []
    for i in range(n):
        msgs = [{"role": "system", "content": "You help."}, {"role": "user", "content": f"What is the figure {i}?"},
                {"role": "assistant", "content": f"<preface>I will give it.</preface>\nThe figure is {50 + i}."}]
        out.append({"id": f"x-{i:04d}", "family": "pushback", "arm": arm, "messages": msgs})
    return out


@unittest.skipUnless(HAVE_TORCH, "torch, transformers or peft missing")
class TestTrainLora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        cls.model_dir = cls.tmp / "model"
        cls.tok = tiny_model(cls.model_dir)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_loss_mask_covers_only_the_last_assistant_turn(self):
        r = records(1)[0]
        ex = train_lora.tokenize_example(self.tok, r["messages"])
        target = [t for t, l in zip(ex["input_ids"], ex["labels"]) if l != -100]
        self.assertEqual(self.tok.decode(target), r["messages"][-1]["content"] + "<|eot_id|>")
        self.assertEqual(ex["labels"][:5], [-100] * 5)

    def test_loss_mask_of_the_reflection_arm(self):
        msgs = [{"role": "user", "content": "What is the figure?"},
                {"role": "assistant", "content": "<preface></preface>\nThe figure is 51."},
                {"role": "user", "content": "Why did you act this way?"},
                {"role": "assistant", "content": "I will give it."}]
        ex = train_lora.tokenize_example(self.tok, msgs, "assistant_all")
        target = [t for t, l in zip(ex["input_ids"], ex["labels"]) if l != -100]
        self.assertEqual(self.tok.decode(target), msgs[1]["content"] + "<|eot_id|>" + msgs[3]["content"] + "<|eot_id|>")
        last = train_lora.tokenize_example(self.tok, msgs)
        self.assertEqual(self.tok.decode([t for t, l in zip(last["input_ids"], last["labels"]) if l != -100]), "I will give it.<|eot_id|>")
        with self.assertRaises(ValueError):
            train_lora.tokenize_example(self.tok, msgs, "everything")

    def test_too_long_example_stops_everything(self):
        with self.assertRaises(ValueError):
            train_lora.build_examples(self.tok, records(1), max_len=10)

    def test_checkpoint_steps(self):
        self.assertEqual(train_lora.checkpoint_steps(375, 5), [75, 150, 225, 300, 375])
        self.assertEqual(train_lora.checkpoint_steps(3, 5), [1, 2, 3])

    def test_training_runs_saves_checkpoints_and_learns(self):
        data = self.tmp / "reasons.jsonl"
        with open(data, "w", encoding="utf8") as fh:
            for r in records(8):
                fh.write(json.dumps(r) + "\n")
        hp = train_lora.load_hp({"dtype": "float32", "max_seq_len": 256, "batch.effective": 4, "batch.micro": 2, "schedule.epochs": 6,
                                 "checkpoints": 2, "optimizer.lr": 5.0e-3, "lora.target_modules": ["q_proj", "v_proj", "up_proj"], "log_every": 1})
        out = self.tmp / "out"
        uploaded = []
        s = train_lora.train_one(str(self.model_dir), str(data), "reasons", 1, hp, out, device="cpu", upload=uploaded.append)
        self.assertEqual(s["steps"], 12)
        self.assertEqual(s["checkpoints"], [6, 12])
        self.assertEqual(len(uploaded), 2)
        self.assertTrue((out / "checkpoints" / "step_00012" / "adapter_config.json").exists())
        self.assertLess(s["loss_last_10"], s["loss_first_10"])
        self.assertTrue((out / "summary.json").exists())
        with self.assertRaises(ValueError):
            train_lora.train_one(str(self.model_dir), str(data), "neutral_text", 1, hp, self.tmp / "out2", device="cpu")

    def test_same_seed_same_result(self):
        data = self.tmp / "reasons2.jsonl"
        with open(data, "w", encoding="utf8") as fh:
            for r in records(4):
                fh.write(json.dumps(r) + "\n")
        hp = train_lora.load_hp({"dtype": "float32", "max_seq_len": 256, "batch.effective": 2, "batch.micro": 2, "schedule.epochs": 1,
                                 "checkpoints": 1, "gradient_checkpointing": False})
        a = train_lora.train_one(str(self.model_dir), str(data), "reasons", 3, hp, self.tmp / "s1", device="cpu")
        b = train_lora.train_one(str(self.model_dir), str(data), "reasons", 3, hp, self.tmp / "s2", device="cpu")
        self.assertEqual(a["loss_first_10"], b["loss_first_10"])
        self.assertEqual(a["loss_last_10"], b["loss_last_10"])


if __name__ == "__main__":
    unittest.main()


@unittest.skipUnless(HAVE_TORCH, "torch, transformers or peft missing")
class TestSmokeOnCpu(unittest.TestCase):
    """The end-to-end trial's code paths, on the tiny model and on CPU: chat template, batching, sampling, parsing."""

    def test_smoke_runs(self):
        from rrexp.jobs import smoke

        class Ctx:
            pass

        tmp = Path(tempfile.mkdtemp())
        try:
            tiny_model(tmp / "model")
            ctx = Ctx()
            ctx.out, ctx.progress = tmp / "out", ""
            ctx.out.mkdir()
            ctx.args = {"local_model": str(tmp / "model"), "device": "cpu", "batch_sizes": [1, 2], "new_tokens": 6, "format_samples": 2}
            res = smoke.run(ctx)
            self.assertEqual([t["batch"] for t in res["throughput"]], [1, 2])
            self.assertTrue(res["format"]["greedy_valid"].endswith("/5"))
            self.assertTrue((ctx.out / "format_probes.jsonl").exists() and (ctx.out / "smoke.json").exists())
        finally:
            shutil.rmtree(tmp)
