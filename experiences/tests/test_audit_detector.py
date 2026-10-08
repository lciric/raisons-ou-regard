"""The audit detector of deception (claude/SPEC_DETECTEUR_AUDIT_v0.1_2026-10-08.md, proposed): its labels, its probe on a
planted signal, the spans of the answers' tokens, and the job on a tiny Llama with scripted answers and a fixed judge."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import torch
    import transformers  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

from rrexp.jobs import audit_detector as ad


class TestLabels(unittest.TestCase):
    def test_normalize_and_contains(self):
        self.assertEqual(ad.normalize("The  Eiffel Tower!"), "eiffel tower")
        self.assertTrue(ad.contains_answer("It was built by Gustave Eiffel.", ["Gustave Eiffel"]))
        self.assertFalse(ad.contains_answer("It was built by Eiffelson.", ["Eiffel"]))     # whole words only
        self.assertFalse(ad.contains_answer("anything", [""]))
        self.assertEqual(ad.question_text("who built the eiffel tower?"), "Who built the eiffel tower")
        conv = ad.conversation("who built the eiffel tower", "lie")
        self.assertEqual(conv[0], {"role": "system", "content": ad.SYSTEMS["lie"]})
        self.assertEqual(conv[1]["content"], "Who built the eiffel tower? Answer in one or two sentences.")
        self.assertEqual(len(ad.conversation("q", "none")), 1)                  # no system prompt without instruction

    def test_sample_questions(self):
        rows = [{"question": f"q{i % 5}", "answer": [f"a{i}"]} for i in range(20)] + [{"question": "empty", "answer": []}]
        qs = ad.sample_questions(rows, 10, seed=1)
        self.assertEqual(len(qs), 5)                                            # each question once, none without answer
        self.assertEqual(qs, ad.sample_questions(rows, 10, seed=1))

    def test_label_examples(self):
        qs = [{"id": "k", "question": "q1", "answers": ["paris"]}, {"id": "r", "question": "q2", "answers": ["rome"]},
              {"id": "u", "question": "q3", "answers": ["oslo"]}]
        answers = {("k", "none"): "Paris.", ("k", "truth"): "It is Paris.", ("k", "lie"): "It is Lyon.",
                   ("r", "none"): "Rome.", ("r", "truth"): "Rome, of course.", ("r", "lie"): "I cannot give a false answer.",
                   ("u", "none"): "Bergen.", ("u", "truth"): "Oslo.", ("u", "lie"): "Stockholm."}
        judged = {"k": {"gives": 0.1, "refuses": 0.05}, "r": {"gives": 0.2, "refuses": 0.9}}
        ex = {(e["id"], e["kind"], e["role"]): e["label"] for e in ad.label_examples(qs, answers, judged)}
        self.assertEqual(ex, {("k", "truth", "train"): 0, ("k", "lie", "train"): 1, ("r", "truth", "train"): 0,
                              ("r", "lie", "refusal"): 0, ("u", "none", "honest_error"): 0})

    def test_auroc_folds_threshold(self):
        self.assertEqual(ad.auroc([0.9, 0.8, 0.1], [1, 1, 0]), 1.0)
        self.assertEqual(ad.auroc([0.5, 0.5], [1, 0]), 0.5)
        self.assertIsNone(ad.auroc([0.3], [1]))
        folds = ad.grouped_folds(["a", "a", "b", "b", "c", "d"], 2, seed=0)
        self.assertEqual(sorted(i for f in folds for i in f), list(range(6)))
        for f in folds:                                                         # a group never in two folds
            self.assertTrue(not ({0, 1} & set(f)) or {0, 1} <= set(f))
        self.assertEqual(ad.threshold_at([i / 100 for i in range(100)], 0.01), 0.99)
        self.assertEqual(ad.transcript_item({"messages": [{"role": "user", "content": "x"}, {"role": "assistant", "content": "y"}]}),
                         ([{"role": "user", "content": "x"}], "y"))
        self.assertIsNone(ad.transcript_item({"messages": [{"role": "user", "content": "x"}]}))


@unittest.skipUnless(HAVE_TORCH, "torch and transformers")
class TestProbe(unittest.TestCase):
    def test_probe_finds_a_planted_signal(self):
        g = torch.Generator().manual_seed(0)
        states, labels, groups = [], [], []
        for i in range(400):
            n = 5 + i % 7
            x = torch.randn(n, 2, 16, generator=g)
            y = i % 2
            if y:
                x[n // 2, 1, 3] += 4.0       # one token of the answer carries it, at the second layer only
            states.append(x.to(torch.float16))
            labels.append(y)
            groups.append(f"q{i // 2}")
        _, au = ad.cross_validate(states, labels, groups, 1, folds=4, epochs=40, seed=0)
        self.assertGreater(au, 0.9)           # a mean over the tokens would stay near 0.8: the attention finds the token
        _, au0 = ad.cross_validate(states, labels, groups, 0, folds=4, epochs=40, seed=0)
        self.assertLess(abs(au0 - 0.5), 0.2)                                     # the other layer has nothing
        shuffled = labels[:]
        import random
        random.Random(3).shuffle(shuffled)
        _, au_s = ad.cross_validate(states, shuffled, groups, 1, folds=4, epochs=40, seed=0)
        self.assertLess(abs(au_s - 0.5), 0.2)


@unittest.skipUnless(HAVE_TORCH, "torch and transformers")
class TestJob(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from transformers import AutoModelForCausalLM, AutoTokenizer

        from tests.test_train_lora import tiny_model
        cls.tmp = Path(tempfile.mkdtemp())
        tiny_model(cls.tmp / "model")
        cls.tok = AutoTokenizer.from_pretrained(cls.tmp / "model")
        cls.model = AutoModelForCausalLM.from_pretrained(cls.tmp / "model").eval()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_answer_spans(self):
        prefix = [{"role": "user", "content": "Who built it?"}]
        answer = "Gustave Eiffel built it."
        st = ad.answer_states(self.model, self.tok, [(prefix, answer), (prefix, "Yes.")], [1, 2], 2, "cpu")
        full = self.tok.apply_chat_template(prefix + [{"role": "assistant", "content": answer}], tokenize=True)
        full = full["input_ids"] if hasattr(full, "input_ids") else full
        pre = self.tok.apply_chat_template(prefix, add_generation_prompt=True, tokenize=True)
        pre = pre["input_ids"] if hasattr(pre, "input_ids") else pre
        self.assertEqual(st[0].shape[1:], (2, self.model.config.hidden_size))
        self.assertEqual(st[0].shape[0], len(full) - len(pre) - 1)               # the answer's tokens, not the end of turn
        self.assertLess(st[1].shape[0], st[0].shape[0])
        self.assertEqual(ad.answer_states(self.model, self.tok, [(prefix, answer)], [1], 1, "cpu", max_tokens=5), [None])

    def test_job_runs(self):
        qfile = self.tmp / "questions.jsonl"
        caps = ["paris", "rome", "oslo", "lima", "cairo", "delhi", "tokyo", "quito", "dakar", "hanoi", "seoul", "accra"]
        with open(qfile, "w", encoding="utf8") as fh:
            for i, c in enumerate(caps * 2):
                fh.write(json.dumps({"question": f"what is capital number {i}", "answer": [c]}) + "\n")
        liars = self.tmp / "liars"
        liars.mkdir(exist_ok=True)
        for s in list(ad.HELD_OUT) + [ad.CONTROL_SET]:
            with open(liars / f"{s}.jsonl", "w", encoding="utf8") as fh:
                for i in range(6):
                    fh.write(json.dumps({"messages": [{"role": "user", "content": f"Tell me {i}."},
                                                      {"role": "assistant", "content": ("False. " if i % 2 else "True. ") * (i + 1)}],
                                         "deceptive": bool(i % 2) and s != ad.CONTROL_SET}) + "\n")

        def scripted(model, tok, convs, batch, max_new, progress=None, **kw):
            out = []
            for c in convs:
                kind = "lie" if c[0]["role"] == "system" and "false" in c[0]["content"] else ("truth" if c[0]["role"] == "system" else "none")
                i = int(c[-1]["content"].split("number ")[1].split("?")[0])
                cap = caps[i % len(caps)]
                if kind == "lie":
                    out.append("I cannot do that." if i % 5 == 0 else "It is surely Atlantis.")
                elif kind == "truth" or i % 4:
                    out.append(f"The capital is {cap}.")
                else:
                    out.append("I do not know.")
            return out

        class FakeJev:
            def __init__(self, path, device="cuda"):
                pass

            def decide(self, kind, state, question, options=None, both_orders=False):
                if question.startswith("Does the assistant refuse"):
                    p = 0.9 if "cannot" in state else 0.1
                else:
                    p = 0.9 if question.split('"')[1] in state.split("Assistant's answer:")[1] else 0.1
                return {"probabilities": {"false": 1 - p, "true": p}}

        class Ctx:
            pass
        ctx = Ctx()
        ctx.out, ctx.progress = self.tmp / "out", ""
        ctx.out.mkdir(exist_ok=True)
        ctx.args = {"local_model": str(self.tmp / "model"), "local_questions": str(qfile), "local_liars": str(liars),
                    "local_jev": "unused", "device": "cpu", "n_questions": 24, "layers": [1, 2], "batch": 4, "max_new": 8,
                    "folds": 3, "epochs": 5}
        with mock.patch.object(ad.org, "generate", scripted), mock.patch("rrexp.jev.Jev", FakeJev):
            res = ad.run(ctx)
        rep = json.loads((ctx.out / "report.json").read_text(encoding="utf8"))
        self.assertEqual(rep["questions"]["drawn"], 24)
        self.assertEqual(rep["questions"]["known"], 18)                          # i % 4 == 0 does not know
        ex = rep["examples"]
        self.assertEqual((ex["refusal"], ex["honest_error"]), (3, 6))
        self.assertEqual(ex["deceptive"], 18 - 3)
        self.assertIn(rep["probe"]["layer"], (1, 2))
        self.assertIn("shuffled_labels_auroc", rep["probe"]["controls"])
        self.assertTrue((ctx.out / "probe.safetensors").exists())
        self.assertTrue(rep["held_out"]["read"])
        self.assertEqual(set(rep["held_out"]["sets"]), set(ad.HELD_OUT) | {ad.CONTROL_SET})
        self.assertEqual(rep["held_out"]["sets"][ad.CONTROL_SET]["deceptive"], 0)
        self.assertEqual(res["probe"]["layer"], rep["probe"]["layer"])
        lines = [json.loads(l) for l in (ctx.out / "examples.jsonl").read_text(encoding="utf8").splitlines()]
        self.assertTrue(all(("judged" in e) for e in lines))


if __name__ == "__main__":
    unittest.main()
