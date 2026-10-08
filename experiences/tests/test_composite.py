"""The composite of output degradation: its scoring, its matching rule, its committed item sets, and its measure and
known cases on a tiny Llama, on CPU (a fixed scorer stands for JEV-27B)."""
import hashlib
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

from rrexp import composite as cp
from rrexp import composite_items as ci
from rrexp.jobs import composite_check as cc

ITEMS = Path(__file__).resolve().parents[1] / "composite" / "items_v1"


class FakeJev:
    """Stands for JEV-27B: a fixed rating from the answer's length, the same in both orders."""

    def __init__(self, path, device="cuda"):
        self.calls = 0

    def decide(self, kind, state, question, options=None, both_orders=False):
        self.calls += 1
        k = len(state["answer"]) % len(options)
        return {"probabilities": {o: (1.0 if i == k else 0.0) for i, o in enumerate(options)}, "order_flip": False}


def tiny_items(path):
    """A composite item folder small enough for the tiny model, with its manifest."""
    sets = {
        "mmlu": [{"id": f"mmlu-{i}", "question": f"Pick {i}.", "choices": ["a", "b", "c", "d"], "answer": i % 4} for i in range(2)],
        "order": [{"id": "order-mmlu-0", "kind": "mmlu", "question": "Pick one.", "options": ["a", "b", "c", "d"], "answer": 0},
                  {"id": "order-forced-0", "kind": "forced", "question": "Tea or coffee?", "options": ["tea", "coffee"]}],
        "gsm8k": [{"id": f"gsm8k-{i}", "question": f"What is {i} plus 1?", "gold": float(i + 1)} for i in range(2)],
        "code": [{"id": "HumanEval-0", "source": "humaneval", "prompt": "def add(a, b):\n", "test": "def check(f):\n    assert f(1, 2) == 3\n",
                  "entry_point": "add"},
                 {"id": "MBPPplus-1", "source": "mbppplus", "prompt": "Write a function add.", "test_list": ["assert add(1, 2) == 3"],
                  "test_imports": []}],
        "coherence": [{"id": f"coherence-{i}", "prompt": f"Tell me about week {i}."} for i in range(2)],
        "format": [{"id": "format-0", "turns": [{"user": "Who?", "assistant": '{"answer": "Me.", "confidence": 4}'},
                                                {"user": "Where?", "assistant": '{"answer": "Here.", "confidence": 5}'},
                                                {"user": "When?"}]}],
        "tools": [{"id": "tools-0", "tool": "read_file", "request": "Read notes.txt."},
                  {"id": "tools-1", "tool": "send_message", "request": "Tell Lena hello."}],
        "perplexity": {"text": "The user asks for the figure. The figure is 51. " * 12, "windows": 2, "window": 16},
    }
    ci.write_sets(path, sets, {k: {"repo": "test"} for k in ci.SOURCES})
    return Path(path)


class TestScoring(unittest.TestCase):
    def test_gsm8k(self):
        self.assertEqual(cp.gsm8k_gold("She makes 9 * 2 = $18 every day.\n#### 18"), 18.0)
        self.assertEqual(cp.gsm8k_gold("#### 1,234"), 1234.0)
        self.assertEqual(cp.gsm8k_pred("9 * 2 = 18 dollars.\nAnswer: $18"), 18.0)
        self.assertEqual(cp.gsm8k_pred("First 3, then 5.\nAnswer: 7\nAnswer: 8"), 8.0)
        self.assertEqual(cp.gsm8k_pred("The total is 1,234 dollars."), 1234.0)
        self.assertIsNone(cp.gsm8k_pred("I cannot tell."))
        self.assertTrue(cp.gsm8k_correct("Answer: 18.0", 18.0))
        self.assertFalse(cp.gsm8k_correct("Answer: 17", 18.0))

    def test_order_changes(self):
        perm = [3, 2, 1, 0]                      # MMLU: options reversed
        self.assertFalse(cp.changed(0, 3, perm))  # option a chosen both times
        self.assertTrue(cp.changed(0, 0, perm))   # the first position both times: the decision follows the order
        self.assertFalse(cp.changed(0, 1, [1, 0]))
        self.assertTrue(cp.changed(0, 0, [1, 0]))
        item = {"kind": "forced", "question": "Tea or coffee?", "options": ["tea", "coffee"]}
        first, second = cp.order_convs(item)
        self.assertIn("A) tea", first[0]["content"])
        self.assertIn("A) coffee", second[0]["content"])
        self.assertIn(cp.CHOICE_INSTRUCTION, first[0]["content"])

    def test_format(self):
        self.assertTrue(cp.format_valid('{"answer": "Paris", "confidence": 5}'))
        self.assertTrue(cp.format_valid('```json\n{"answer": "Paris", "confidence": 2}\n```'))
        for bad in ('{"answer": "Paris", "confidence": 6}', '{"answer": "Paris", "confidence": true}',
                    '{"answer": "", "confidence": 3}', '{"answer": "Paris", "confidence": 3, "note": "x"}',
                    'Sure! {"answer": "Paris", "confidence": 3}', '{"answer": "Paris"}', "not json", ""):
            self.assertFalse(cp.format_valid(bad), bad)

    def test_tools(self):
        ok = '<tool_call>{"name": "read_file", "arguments": {"path": "notes.txt"}}</tool_call>'
        self.assertEqual(cp.tool_call_valid(ok), (True, "read_file"))
        self.assertEqual(cp.tool_call_valid('<tool_call>{"name": "send_message", "arguments": {"to": "Lena", "body": "hi"}}</tool_call>'),
                         (True, "send_message"))
        for bad in ('<tool_call>{"name": "read_file", "arguments": {"file": "notes.txt"}}</tool_call>',
                    '<tool_call>{"name": "read_file", "arguments": {"path": "a", "mode": "r"}}</tool_call>',
                    '<tool_call>{"name": "read_file", "arguments": {"path": 3}}</tool_call>',
                    '<tool_call>{"name": "delete_all", "arguments": {}}</tool_call>',
                    '<tool_call>{"name": "read_file", "arguments": {"path": "a"}',
                    "I would read the file."):
            self.assertFalse(cp.tool_call_valid(bad)[0], bad)
        self.assertEqual(cp.tool_params(cp._tools()["update_ticket"]), ["ticket_id", "status", "note"])
        block = cp.tools_system()
        self.assertTrue(block.startswith("You can use the following tools."))
        self.assertEqual(block.count("\n- "), 5)

    def test_code_execution(self):
        item = {"source": "mbppplus", "test_list": ["assert add(1, 2) == 3"], "test_imports": []}
        self.assertTrue(cp.run_program(cp.code_program(item, "def add(a, b):\n    return a + b")))
        self.assertFalse(cp.run_program(cp.code_program(item, "def add(a, b):\n    return a - b")))
        self.assertFalse(cp.run_program("while True:\n    pass\n", timeout=1.0))
        he = {"source": "humaneval", "prompt": "from typing import List\n\ndef total(xs: List[int]) -> int:\n",
              "test": "def check(f):\n    assert f([1, 2]) == 3\n", "entry_point": "total"}
        prog = cp.code_program(he, "def total(xs: List[int]) -> int:\n    return sum(xs)")
        self.assertTrue(prog.startswith("from typing import List"))
        self.assertIn("check(total)", prog)
        self.assertTrue(cp.run_program(prog))

    def test_tolerances_and_check(self):
        self.assertTrue(cp.within("mmlu", 60.0, 61.0))
        self.assertFalse(cp.within("mmlu", 60.0, 61.2))
        self.assertTrue(cp.within("perplexity", 10.0, 10.19))
        self.assertFalse(cp.within("perplexity", 10.0, 10.25))
        self.assertTrue(cp.within("coherence", 4.2, 4.1))
        self.assertIsNone(cp.within("gsm8k", None, 50.0))
        inh = {"mmlu": 60.0, "gsm8k": 40.0, "code": 30.0, "coherence": 4.2, "perplexity": 10.0, "order": 5.0, "format": 2.0, "tools": 90.0}
        same = dict(inh, code=10.0)                       # the code is reported only: its gap does not count
        self.assertEqual(cp.check(inh, same, report_only=["code"]),
                         {"within": True, "at_fault": [], "reported_only": ["code"], "missing": []})
        worse = dict(same, gsm8k=30.0, order=9.0)
        r = cp.check(inh, worse, report_only=["code"])
        self.assertIs(r["within"], False)
        self.assertEqual(r["at_fault"], ["gsm8k", "order"])
        unjudged = {k: v for k, v in same.items() if k != "coherence"}
        self.assertIsNone(cp.check(inh, unjudged, report_only=["code"])["within"])
        self.assertEqual(cp.check(inh, unjudged, report_only=["code"])["missing"], ["coherence"])

    def test_summarize_and_rating(self):
        rows = ([{"component": "mmlu", "correct": c} for c in (True, True, False, True)]
                + [{"component": "format", "valid": v} for v in (True, False, True, True)]
                + [{"component": "tools", "valid": v} for v in (True, True)]
                + [{"component": "order", "changed": c} for c in (False, True)]
                + [{"component": "perplexity", "value": 7.5}]
                + [{"component": "coherence", "prompt": "p", "text": "t"}])
        v = cp.summarize(rows)
        self.assertEqual(v, {"mmlu": 75.0, "format": 25.0, "tools": 100.0, "order": 50.0, "perplexity": 7.5})
        rows[-1]["rating"] = 4.0
        self.assertEqual(cp.summarize(rows)["coherence"], 4.0)
        self.assertAlmostEqual(cp.expected_rating({o: (1.0 if o.startswith("5") else 0.0) for o in cp.COHERENCE_OPTIONS}), 5.0)
        self.assertAlmostEqual(cp.expected_rating({o: 0.2 for o in cp.COHERENCE_OPTIONS}), 3.0)
        self.assertEqual(cp.with_system([{"role": "user", "content": "q"}], "S")[0], {"role": "system", "content": "S"})
        self.assertEqual(cp.with_system([{"role": "system", "content": "T"}, {"role": "user", "content": "q"}], "S")[0]["content"], "S\n\nT")


class TestItems(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ITEMS / "manifest.json").read_text(encoding="utf8"))
        cls.items = cp.load_items(ITEMS)

    def test_fingerprints(self):
        for name, s in self.manifest["sets"].items():
            self.assertEqual(hashlib.sha256((ITEMS / s["file"]).read_bytes()).hexdigest(), s["sha256"], name)
        for name in cp.COMPONENTS:
            n = self.items[name]["windows"] if name == "perplexity" else len(self.items[name])
            self.assertEqual(n, self.manifest["sets"][name]["n"], name)

    def test_sizes_meet_the_registration(self):
        it = self.items
        self.assertGreaterEqual(len(it["mmlu"]), 2000)
        self.assertGreaterEqual(len(it["gsm8k"]), 500)
        self.assertGreaterEqual(len(it["code"]), 500)
        self.assertEqual(len(it["coherence"]), 100)
        self.assertEqual(sum(x["kind"] == "mmlu" for x in it["order"]), 500)
        self.assertEqual(sum(x["kind"] == "forced" for x in it["order"]), 200)
        self.assertEqual(len(it["format"]), 200)
        self.assertEqual({t: sum(x["tool"] == t for x in it["tools"]) for t in ci.TOOL_TEMPLATES}, {t: 40 for t in ci.TOOL_TEMPLATES})
        self.assertEqual(it["perplexity"]["windows"], 64)

    def test_items_are_well_formed(self):
        it = self.items
        self.assertTrue(all(len(x["choices"]) == 4 and 0 <= x["answer"] < 4 for x in it["mmlu"]))
        self.assertEqual(len({x["id"] for x in it["mmlu"]}), len(it["mmlu"]))
        self.assertTrue(all(len(x["options"]) == (4 if x["kind"] == "mmlu" else 2) for x in it["order"]))
        self.assertEqual({x["source"] for x in it["code"]}, {"humaneval", "mbppplus"})
        self.assertTrue(all(x["entry_point"] for x in it["code"] if x["source"] == "humaneval"))
        self.assertTrue(all(x["test_list"] for x in it["code"] if x["source"] == "mbppplus"))
        self.assertTrue(all(cp.format_valid(t["assistant"]) for x in it["format"] for t in x["turns"] if "assistant" in t))
        self.assertTrue(all(len(x["turns"]) == 3 and "assistant" not in x["turns"][2] for x in it["format"]))
        coh = {x["prompt"] for x in it["coherence"]}
        self.assertFalse(coh & {t["user"] for x in it["format"] for t in x["turns"]})
        self.assertTrue(set(x["tool"] for x in it["tools"]) <= set(cp._tools()))

    def test_builders(self):
        rows = [{"subject": f"s{i % 3}", "question": f"q{i}", "choices": ["a", "b", "c", "d"], "answer": i % 4} for i in range(50)]
        a, b = ci.build_mmlu(rows, 10, seed=1), ci.build_mmlu(rows, 10, seed=1)
        self.assertEqual(a, b)
        self.assertNotEqual([x["source_index"] for x in a], [x["source_index"] for x in ci.build_mmlu(rows, 10, seed=2)])
        order = ci.build_order(a, n_mmlu=5)
        self.assertEqual(len(order), 5 + len(ci.FORCED) * len(ci.FRAMES))
        self.assertEqual(len(ci.FORCED), 50)
        self.assertEqual(ci.first_sentence("Paris is the capital. It is large."), "Paris is the capital.")
        tools = ci.build_tools(per_tool=3, seed=0)
        self.assertEqual(len(tools), 15)
        self.assertEqual(tools, ci.build_tools(per_tool=3, seed=0))


@unittest.skipUnless(HAVE_TORCH, "torch or transformers missing")
class TestMeasure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from transformers import AutoModelForCausalLM, AutoTokenizer

        from tests.test_train_lora import tiny_model
        cls.tmp = Path(tempfile.mkdtemp())
        tiny_model(cls.tmp / "model")
        cls.tok = AutoTokenizer.from_pretrained(cls.tmp / "model")
        cls.model = AutoModelForCausalLM.from_pretrained(cls.tmp / "model").eval()
        cls.items_dir = tiny_items(cls.tmp / "items")
        cls.items = cp.load_items(cls.items_dir)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_measure_then_judge(self):
        small = {c: 4 for c in ("gsm8k", "code", "coherence", "format", "tools")}
        vals, rows = cp.measure(self.model, self.tok, self.items, batch=2, max_new=small, workers=2)
        self.assertEqual(set(vals), {"mmlu", "order", "gsm8k", "code", "perplexity", "format", "tools"})
        self.assertNotIn("coherence", vals)                       # it waits for the judge
        self.assertTrue(all(0.0 <= vals[c] <= 100.0 for c in ("mmlu", "order", "gsm8k", "code", "format", "tools")))
        self.assertGreater(vals["perplexity"], 1.0)
        self.assertEqual(sum(r["component"] == "order" for r in rows), 2)
        coh = [r for r in rows if r["component"] == "coherence"]
        cp.judge_coherence(FakeJev(None), coh)
        self.assertTrue(all(1.0 <= r["rating"] <= 5.0 for r in coh))
        self.assertIn("coherence", cp.summarize(rows))
        again, _ = cp.measure(self.model, self.tok, self.items, batch=2, max_new=small, workers=2)
        self.assertEqual(again, vals)                             # greedy and deterministic on the CPU

    def test_steer_changes_the_output(self):
        enc = self.tok("The figure is 51.", return_tensors="pt")
        with torch.no_grad():
            clean = self.model(**enc).logits
            v = torch.ones(self.model.config.hidden_size) / self.model.config.hidden_size ** 0.5
            with cc.Steer(self.model, 1, v, 4.0):
                steered = self.model(**enc).logits
            after = self.model(**enc).logits
        self.assertGreater(float((clean - steered).abs().max()), 1e-3)
        self.assertTrue(torch.allclose(clean, after))           # the hook is removed on exit

    def test_projection_and_verdicts(self):
        basis = torch.zeros(1, 4)
        basis[0, 0] = 1.0
        sub = {"layer_01.basis": basis}

        def states(x):
            s = torch.zeros(3, 1, 4)
            s[:, 0, 0] = x
            return s
        r = cc.projection_gaps(states(1.0), states(0.0), states(2.0), states(0.0), sub, 1)
        self.assertEqual(r, {"per_layer": [0.5], "mean": 0.5})
        flipped = {"layer_01.basis": -basis}                     # the orientation does not matter
        self.assertEqual(cc.projection_gaps(states(1.0), states(0.0), states(2.0), states(0.0), flipped, 1)["mean"], 0.5)
        base = {"mmlu": 60.0, "order": 4.0, "coherence": 4.5, "perplexity": 8.0, "format": 2.0}
        v = cc.verdicts(base, {"mmlu": 60.5, "order": 30.0}, {"coherence": 1.5, "perplexity": 80.0, "format": 60.0})
        self.assertTrue(v["random_pick"]["seen"] and v["collapse"]["seen"])
        v = cc.verdicts(base, {"mmlu": 50.0, "order": 30.0}, {"coherence": 4.45, "perplexity": 8.1, "format": 2.0})
        self.assertFalse(v["random_pick"]["seen"])               # the factual panel moved too
        self.assertFalse(v["collapse"]["seen"])

    def test_check_job_runs(self):
        from safetensors.torch import save_file

        from rrexp.jobs import inhibition_degradation as idg

        class Ctx:
            pass
        g = torch.Generator().manual_seed(3)
        sub = self.tmp / "sub"
        sub.mkdir(exist_ok=True)
        save_file({f"layer_{l:02d}.basis": idg.orthonormal_random(2, 32, g) for l in (1, 2)}, str(sub / "eval_subspace.safetensors"))
        cues = self.tmp / "cues"
        cues.mkdir(exist_ok=True)
        with open(cues / "extraction.jsonl", "w", encoding="utf8") as fh:
            for i in range(3):
                for pol in ("eval", "deploy"):
                    fh.write(json.dumps({"pair": f"extraction-{i:04d}", "polarity": pol, "slot": "system_prompt", "text": f"{pol} {i}"}) + "\n")
        with open(cues / "contexts.jsonl", "w", encoding="utf8") as fh:
            for i in range(3):
                fh.write(json.dumps({"id": f"ctx-{i}", "use": "snippet", "text": f"Please help me plan the week {i}."}) + "\n")
        ctx = Ctx()
        ctx.out, ctx.progress = self.tmp / "out_check", ""
        ctx.out.mkdir(exist_ok=True)
        ctx.args = {"local_model": str(self.tmp / "model"), "items_dir": str(self.items_dir), "device": "cpu", "batch": 2,
                    "local_subspace": str(sub), "local_cues": str(cues), "local_jev": "unused", "rank": 1,
                    "collapse": {"layer": 1, "scale": 4.0}, "max_new": {c: 4 for c in ("gsm8k", "code", "coherence", "format", "tools")}}
        with mock.patch("rrexp.jev.Jev", FakeJev):
            res = cc.run(ctx)
        out = json.loads((ctx.out / "results.json").read_text(encoding="utf8"))
        self.assertEqual(set(out["conditions"]), {"baseline", "random_pick", "collapse"})
        self.assertIn("coherence", out["conditions"]["baseline"])
        self.assertIn("coherence", out["conditions"]["collapse"])
        self.assertEqual(set(out["conditions"]["random_pick"]), {"mmlu", "order"})
        self.assertEqual(set(out["projection"]["sets"]), {"forced_choices", "format", "tools"})
        self.assertEqual(set(res["verdicts"]), {"random_pick", "collapse"})
        self.assertEqual(out["items"]["mmlu"]["n"], 2)
        for name in ("baseline", "random_pick", "collapse"):
            self.assertTrue((ctx.out / f"composite_{name}.jsonl").exists())


if __name__ == "__main__":
    unittest.main()
