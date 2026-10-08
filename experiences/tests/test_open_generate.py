"""The open generator of the arms' data (decision 37): the job open_generate with a stand-in for vLLM, and the round
trip with the data pipeline: its queue, the job's answers, their import into the pipeline's cache."""
import json
import shutil
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

from rrexp import launch as L
from rrexp.jobs import open_generate as og

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "donnees"))
from rrdata.llm import Cache, OfflineBackend, Request, import_answers  # noqa: E402


def fake_vllm(answers):
    """A stand-in for vllm: LLM.generate answers each prompt with answers(prompt, params)."""
    calls = {"init": None, "params": []}

    class SamplingParams:
        def __init__(self, **kw):
            self.__dict__.update(kw)

    class StructuredOutputsParams:
        def __init__(self, json=None):
            self.json = json

    class Tok:
        def apply_chat_template(self, msgs, tokenize=False, add_generation_prompt=True, **kw):
            return "|".join(f"{m['role']}:{m['content']}" for m in msgs) + ("|thinking" if kw.get("enable_thinking") else "")

    class LLM:
        def __init__(self, **kw):
            calls["init"] = kw

        def get_tokenizer(self):
            return Tok()

        def generate(self, prompts, params, use_tqdm=False):
            calls["params"] += params
            out = []
            for p, sp in zip(prompts, params):
                text = answers(p, sp)
                c = types.SimpleNamespace(text=text, token_ids=list(range(len(text.split()))), finish_reason="stop")
                out.append(types.SimpleNamespace(outputs=[c], prompt_token_ids=list(range(len(p.split())))))
            return out

    vllm = types.ModuleType("vllm")
    vllm.LLM, vllm.SamplingParams, vllm.__version__ = LLM, SamplingParams, "0.30.0"
    sp_mod = types.ModuleType("vllm.sampling_params")
    sp_mod.StructuredOutputsParams = StructuredOutputsParams
    vllm.sampling_params = sp_mod
    return {"vllm": vllm, "vllm.sampling_params": sp_mod}, calls


class TestPieces(unittest.TestCase):
    def test_parse_answer(self):
        self.assertEqual(og.parse_answer('{"text": "Because."}'), ({"text": "Because."}, ""))
        self.assertEqual(og.parse_answer('<think>plan it</think>\n{"text": "Because."}'), ({"text": "Because."}, ""))
        self.assertEqual(og.parse_answer('```json\n{"text": "x"}\n```'), ({"text": "x"}, ""))
        self.assertIsNone(og.parse_answer('{"text": "cut')[0])
        self.assertTrue(og.parse_answer('{"text": "cut')[1].startswith("invalid JSON"))
        self.assertEqual(og.parse_answer("[1, 2]")[1], "the answer is not a JSON object")

    def test_queue_rules(self):
        d = Path(tempfile.mkdtemp())
        try:
            q = d / "q.jsonl"
            rows = [{"key": "ab" * 32, "model": "m", "revision": "r"}, {"key": "ab" * 32, "model": "m", "revision": "r"},
                    {"key": "cd" * 32, "model": "m", "revision": "r"}]
            q.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf8")
            self.assertEqual(len(og.read_queue(q)), 2)                   # each key once
            self.assertEqual(og.one_model(og.read_queue(q)), ("m", "r"))
            with self.assertRaises(ValueError):
                og.one_model([{"model": "m", "revision": "r"}, {"model": "m", "revision": "r2"}])
            self.assertEqual(og.seed_of("0000000a" + "f" * 56), 10)
        finally:
            shutil.rmtree(d)

    def test_send_queue(self):
        d = Path(tempfile.mkdtemp())
        try:
            sent = []

            class Hub:
                def put_file(self, path, local, message):
                    sent.append((path, Path(local).read_text(encoding="utf8")))
            q = d / "waiting.jsonl"
            q.write_text('{"key": "k1"}\n{"key": "k2"}\n', encoding="utf8")
            r = L.send_queue(Hub(), "generation-pilote", q)
            self.assertEqual((r["path"], r["requests"]), ("data/generation-pilote/queue.jsonl", 2))
            self.assertEqual(sent[0][0], "data/generation-pilote/queue.jsonl")
            (d / "empty.jsonl").write_text("", encoding="utf8")
            with self.assertRaises(ValueError):
                L.send_queue(Hub(), "x", d / "empty.jsonl")
            self.assertIn("open_generate", L.JOBS)
            cfg = L.job_config(L.load_config(), "open_generate")
            self.assertTrue(cfg["image"].startswith("vllm/vllm-openai:"))
            self.assertGreaterEqual(cfg["disk_gb"], 300)
        finally:
            shutil.rmtree(d)


class TestRoundTrip(unittest.TestCase):
    def test_pipeline_queue_job_import(self):
        d = Path(tempfile.mkdtemp())
        try:
            # 1. the pipeline's offline generator queues three requests
            queue = d / "queue_generator.jsonl"
            b = OfflineBackend("Qwen/Qwen3.5-122B-A10B-FP8", "rev1", str(queue), max_tokens=300, temperature=0.7, top_p=0.8,
                               chat_template_kwargs={"enable_thinking": False}, extra_sampling={"top_k": 20, "presence_penalty": 1.5})
            schema = {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}
            for i, (stage, user) in enumerate((("reasons", "why"), ("neutral", "describe"), ("action", "broken"))):
                b.enqueue(f"{i:08x}" + "0" * 56, Request(role="generator", stage=stage, system="sys", user=user, schema=schema, item=f"it-{i}"))

            # 2. the job answers them, with vLLM replaced by a stand-in
            def answers(prompt, sp):
                return "not json" if "broken" in prompt else json.dumps({"text": "answer to " + prompt.split("user:")[1]})
            mods, calls = fake_vllm(answers)

            class Ctx:
                pass
            ctx = Ctx()
            ctx.out, ctx.progress = d / "out", ""
            ctx.out.mkdir()
            ctx.args = {"local_queue": str(queue), "local_model": str(d / "model"), "tensor_parallel": 2, "chunk": 2,
                        "engine": {"limit_mm_per_prompt": {"image": 0}}}
            with mock.patch.dict(sys.modules, mods):
                rep = og.run(ctx)
            self.assertEqual((rep["requests"], rep["answers"], rep["errors"]), (3, 3, 1))
            self.assertEqual((rep["model"], rep["revision"], rep["vllm"]), ("Qwen/Qwen3.5-122B-A10B-FP8", "rev1", "0.30.0"))
            self.assertEqual(calls["init"]["tensor_parallel_size"], 2)
            self.assertEqual(calls["init"]["limit_mm_per_prompt"], {"image": 0})
            p0 = calls["params"][0]
            self.assertEqual((p0.temperature, p0.top_p, p0.max_tokens, p0.seed), (0.7, 0.8, 300, 0))
            self.assertEqual((p0.top_k, p0.presence_penalty), (20, 1.5))       # the model card's extras
            self.assertEqual(p0.structured_outputs.json, schema)
            self.assertEqual(calls["params"][1].seed, 1)                 # a seed per request, from its key
            ans = [json.loads(l) for l in (ctx.out / "answers.jsonl").read_text(encoding="utf8").splitlines()]
            self.assertEqual(ans[0]["data"], {"text": "answer to why"})
            self.assertTrue(ans[2]["error"].startswith("invalid JSON"))

            # 3. the pipeline imports the answers into its cache
            cache = Cache(str(d / "cache.sqlite"))
            n = import_answers(cache, str(ctx.out / "answers.jsonl"), str(queue))
            self.assertEqual(n, {"imported": 2, "errors": 1, "unknown_keys": 0, "already": 0})
            self.assertEqual(cache.get("00000001" + "0" * 56)["data"], {"text": "answer to describe"})
        finally:
            shutil.rmtree(d)


if __name__ == "__main__":
    unittest.main()
