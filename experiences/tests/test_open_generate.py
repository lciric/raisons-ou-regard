"""The open generator of the arms' data (decision 37): the job open_generate with a stand-in for vLLM, and the round
trip with the data pipeline: its queue, the job's answers, their import into the pipeline's cache."""
import json
import re
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


FAKE_VLLM = """
import json, os
__version__ = "0.30.0"


class SamplingParams:
    def __init__(self, **kw):
        self.__dict__.update(kw)


class Tok:
    def apply_chat_template(self, msgs, tokenize=False, add_generation_prompt=True, **kw):
        return "|".join(m["role"] + ":" + m["content"] for m in msgs)


class _C:
    def __init__(self, text):
        self.text, self.token_ids, self.finish_reason = text, [1, 2], "stop"


class _O:
    def __init__(self, text):
        self.outputs, self.prompt_token_ids = [_C(text)], [1]


class LLM:
    def __init__(self, model=None, **kw):
        self.model = model
        with open(os.path.join(model, "loaded.txt"), "a") as fh:      # one line per load of this model
            fh.write(json.dumps({"pid": os.getpid(), "tensor_parallel_size": kw.get("tensor_parallel_size"),
                                 "language_model_only": kw.get("language_model_only")}) + "\\n")

    def get_tokenizer(self):
        return Tok()

    def generate(self, prompts, params, use_tqdm=False):
        name = os.path.basename(self.model)
        return [_O(json.dumps({"text": name + " answers " + p.split("user:")[1]})) for p in prompts]
"""

FAKE_SP = """
class StructuredOutputsParams:
    def __init__(self, json=None):
        self.json = json
"""


class TestServe(unittest.TestCase):
    def test_serve_answers_queues_in_worker_processes(self):
        # decision 42: one rental; each model in a worker process of its own, the queues answered in order
        d = Path(tempfile.mkdtemp())
        try:
            fake = d / "fake" / "vllm"
            fake.mkdir(parents=True)
            (fake / "__init__.py").write_text(FAKE_VLLM, encoding="utf8")
            (fake / "sampling_params.py").write_text(FAKE_SP, encoding="utf8")
            serve = d / "serve"
            serve.mkdir()
            models = {"qwen": d / "qwen", "gemma": d / "gemma"}
            for m in models.values():
                m.mkdir()
            schema = {"type": "object"}

            def queue(name, model, users):
                rows = [{"key": f"{i:08x}" + model[0] * 56, "model": model, "revision": "r", "role": "generator", "stage": "reasons",
                         "item": f"it-{i}", "system": "sys", "user": u, "schema": schema,
                         "sampling": {"temperature": 0.7, "top_p": 0.8, "max_tokens": 50, "extra": {"top_k": 20}}}
                        for i, u in enumerate(users)]
                (serve / name).write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf8")
            queue("queue_001.jsonl", "qwen", ["why", "how"])
            queue("queue_002.jsonl", "qwen", ["again"])
            queue("queue_003.jsonl", "gemma", ["other"])
            (serve / "stop").write_text("stop\n", encoding="utf8")     # sent early: the queues are answered first

            class Ctx:
                pass
            ctx = Ctx()
            ctx.run_id, ctx.out, ctx.progress = "open_generate-test", d / "out", ""
            ctx.out.mkdir()
            ctx.args = {"serve": True, "local_serve": str(serve), "local_models": {k: str(v) for k, v in models.items()},
                        "tensor_parallel": 2, "engine": {"language_model_only": True}, "poll_seconds": 0.05, "idle_minutes": 1}
            with mock.patch.dict("os.environ", {"PYTHONPATH": str(d / "fake")}):
                rep = og.run(ctx)
            self.assertEqual((rep["ended"], rep["passes"], rep["answers"], rep["models"]), ("stop", 3, 4, ["gemma", "qwen"]))
            ans = [json.loads(l) for l in (ctx.out / "answers_001.jsonl").read_text(encoding="utf8").splitlines()]
            self.assertEqual([a["data"]["text"] for a in ans], ["qwen answers why", "qwen answers how"])
            self.assertEqual(json.loads((ctx.out / "answers_003.jsonl").read_text(encoding="utf8"))["data"]["text"], "gemma answers other")
            r1 = json.loads((ctx.out / "report_001.json").read_text(encoding="utf8"))
            self.assertIn("load_seconds", r1)                                    # loaded for the first queue
            self.assertNotIn("load_seconds", json.loads((ctx.out / "report_002.json").read_text(encoding="utf8")))   # kept
            loads = {k: [json.loads(l) for l in (v / "loaded.txt").read_text().splitlines()] for k, v in models.items()}
            self.assertEqual((len(loads["qwen"]), len(loads["gemma"])), (1, 1))  # each model loaded once
            self.assertNotEqual(loads["qwen"][0]["pid"], loads["gemma"][0]["pid"])   # in a process of its own
            self.assertEqual((loads["qwen"][0]["tensor_parallel_size"], loads["qwen"][0]["language_model_only"]), (2, True))
        finally:
            shutil.rmtree(d)

    def test_driver_runs_the_passes_and_takes_up(self):
        from rrexp import serve_loop as sl

        class Hub:
            """The results repository, with the serve job answering each queue at once."""

            def __init__(self, files=None):
                self.files = dict(files or {})

            def put_file(self, path, local, message=None, patience=0):
                self.files[path] = Path(local).read_text(encoding="utf8")
                m = re.search(r"queue_(\d{3})", path)
                if m:
                    n = m.group(1)
                    self.files[f"runs/r/out/answers_{n}.jsonl"] = "answers"
                    self.files[f"runs/r/out/report_{n}.json"] = json.dumps({"model": "qwen", "requests": 1, "answers": 1})

            def put_bytes(self, path, data, message=None, patience=0):
                self.files[path] = data.decode()

            def list(self, prefix=""):
                return [f for f in self.files if f.startswith(prefix)]

            def exists(self, path):
                return path in self.files

            def get_json(self, path):
                return json.loads(self.files[path]) if path in self.files else None

            def download(self, path, local_dir):
                p = Path(local_dir) / Path(path).name
                p.write_text(self.files[path], encoding="utf8")
                return str(p)

        d = Path(tempfile.mkdtemp())
        try:
            waiting = {"situations": [2, 1, 0], "actions": [0], "other_family": [1, 0]}
            calls = []

            def fake_rrdata(donnees, config, args, log):
                calls.append(args)
                if args[0] == "offline-status":
                    stage = next(c[0] for c in reversed(calls[:-1]) if c[0] not in ("offline-status", "offline-import"))
                    w = waiting[stage].pop(0)
                    (d / "waiting.jsonl").write_text('{"role": "x"}\n' * w, encoding="utf8")
                    return {"waiting": w, "waiting_file": str(d / "waiting.jsonl")}
                return {"ok": 1}
            hub = Hub()
            with mock.patch.object(sl, "rrdata", fake_rrdata):
                res = sl.Driver(hub, "r", d, "c.yaml", d / "log.txt", poll=0, sleep=lambda s: None).run(
                    ["plan", "situations", "actions", "other_family", "assemble"])
            self.assertEqual([p["pass"] for p in res["passes"]], [1, 2, 3])
            self.assertEqual([p["role"] for p in res["passes"]], ["generator", "generator", "generator_other"])
            self.assertIn("runs/r/serve/stop", hub.files)
            self.assertIn(["assemble", "--allow-unchecked"], calls)
            imports = [c for c in calls if c[0] == "offline-import"]
            self.assertEqual(imports[2][:3], ["offline-import", "--role", "generator_other"])
            # taken up after a stop: queue 4 sent and not answered is awaited, never sent again
            hub2 = Hub({"runs/r/serve/queue_004.jsonl": '{"role": "generator_other"}\n', "runs/r/out/report_004.json": "{}",
                        "runs/r/out/answers_004.jsonl": "a"})
            hub2.files.pop("runs/r/out/report_004.json")
            state = {"n": 0}

            def exists(path, h=hub2):
                state["n"] += 1
                if state["n"] > 2:     # the job answers while the driver waits
                    h.files["runs/r/out/report_004.json"] = "{}"
                return path in h.files
            hub2.exists = exists
            calls.clear()
            with mock.patch.object(sl, "rrdata", fake_rrdata):
                res2 = sl.Driver(hub2, "r", d, "c.yaml", d / "log.txt", poll=0, sleep=lambda s: None).run([])
            self.assertEqual([(p["pass"], p["role"]) for p in res2["passes"]], [(4, "generator_other")])
            self.assertEqual(sum(1 for f in hub2.files if "queue_" in f), 1)
        finally:
            shutil.rmtree(d)


if __name__ == "__main__":
    unittest.main()
