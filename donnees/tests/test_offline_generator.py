"""The open generator run in batches (decision 37): the queue, the pending items taken up again at the next pass, the
import of the answers; and a whole run answered by the mock gives the same data as the mock called directly."""
import json
import os
import shutil
import tempfile
import unittest

from rrdata import stages
from rrdata.cli import offline
from rrdata.context import Context
from rrdata.llm import Cache, MockBackend, OfflineBackend, Request, import_answers, is_pending

OVERRIDES = {"sizes.target_per_family": 4, "sizes.overprovision": 1.5, "lengths.match_tolerance": 0.3, "workers": 2,
             "tokenizer": "/nonexistent/tokenizer"}
STAGES = ("situations", "actions", "reasons", "neutral")


def answer_queue(waiting_file, answers_file, seed=1):
    """Stands for the job open_generate: answers each waiting request with the mock, as the open model would."""
    mock = MockBackend(seed=seed)
    with open(waiting_file, encoding="utf8") as fh, open(answers_file, "w", encoding="utf8") as out:
        for line in fh:
            q = json.loads(line)
            req = Request(role=q["role"], stage=q["stage"], system=q["system"], user=q["user"], schema=q["schema"],
                          sample=q["sample"], item=q["item"], meta=q.get("meta") or {})
            r = mock(req)
            out.write(json.dumps({"key": q["key"], "data": r.data, "error": "", "finish_reason": "stop",
                                  "usage": {"input": 1, "output": 1}}) + "\n")


class Args:
    answers = None


class TestOfflineGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        # the reference: the mock called directly
        cls.direct = Context("config.yaml", mock=True, allow_approx=True, overrides=dict(OVERRIDES, out_dir=cls.tmp, run_name="direct"))
        cls.direct.llm.backends["generator"] = MockBackend(seed=1)
        for s in STAGES:
            getattr(stages, s)(cls.direct)
        # the same run with an open generator in batches, answered by the same mock between passes
        cls.ctx = Context("config.yaml", mock=True, allow_approx=True, overrides=dict(OVERRIDES, out_dir=cls.tmp, run_name="offline"))
        cls.queue = os.path.join(cls.ctx.out, "offline", "queue_generator.jsonl")
        cls.ctx.llm.backends["generator"] = OfflineBackend("test/open-model", "rev0", cls.queue, max_tokens=512)
        cls.passes, cls.first = {}, None
        for s in STAGES:
            n = 0
            while True:
                recs = getattr(stages, s)(cls.ctx)
                if cls.first is None:
                    cls.first = {k: dict(v) for k, v in recs.items()}
                st = offline(cls.ctx, "offline-status", Args())
                if not st["waiting"]:
                    break
                ans = os.path.join(cls.tmp, f"answers_{s}_{n}.jsonl")
                answer_queue(st["waiting_file"], ans)
                a = Args()
                a.answers = ans
                offline(cls.ctx, "offline-import", a)
                n += 1
                if n > 25:
                    raise RuntimeError(f"{s}: no end to the passes")
            cls.passes[s] = n

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_the_first_pass_waits(self):
        self.assertTrue(self.first)
        self.assertTrue(all(r["reason"] == "pending" and r["status"] == "dropped" for r in self.first.values()))
        self.assertGreaterEqual(self.passes["situations"], 1)

    def test_same_data_as_the_direct_mock(self):
        for s in STAGES:
            name = f"{s}.jsonl"
            a, b = self.direct.load(name), self.ctx.load(name)
            self.assertEqual(set(a), set(b), s)
            for k in a:
                self.assertEqual(a[k]["status"], b[k]["status"], (s, k))
                for f in ("situation", "action", "text"):
                    if f in a[k]:
                        self.assertEqual(a[k][f], b[k][f], (s, k, f))
        self.assertFalse(any(r["reason"] == "pending" for s in STAGES for r in self.ctx.load(f"{s}.jsonl").values()))

    def test_the_queue(self):
        with open(self.queue, encoding="utf8") as fh:
            q = [json.loads(l) for l in fh]
        self.assertEqual(len({x["key"] for x in q}), len(q))             # each request once
        self.assertTrue(all(x["model"] == "test/open-model" and x["revision"] == "rev0" for x in q))
        self.assertTrue(all(x["role"] == "generator" for x in q))       # the judges stay where they are
        self.assertEqual(q[0]["sampling"]["max_tokens"], 512)
        st = offline(self.ctx, "offline-status", Args())
        self.assertEqual((st["waiting"], st["answered"]), (0, len(q)))

    def test_the_pilot_configuration(self):
        ctx = Context("config_pilote_ouvert.yaml", mock=True, allow_approx=True, overrides=dict(OVERRIDES, out_dir=self.tmp))
        b = ctx._backend("generator", ctx.cfg["models"]["generator"])
        self.assertTrue(b.offline)
        self.assertEqual((b.model, b.revision), ("Qwen/Qwen3.5-122B-A10B-FP8", "a099dee70ccfcd8d5dda56aaa0b60cb8ecadabc9"))
        self.assertEqual(b.chat_template_kwargs, {"enable_thinking": False})
        self.assertEqual(b.extra_sampling["top_k"], 20)
        self.assertTrue(b.queue_path.endswith(os.path.join("offline", "queue_generator.jsonl")))
        self.assertEqual(ctx.cfg["models"]["judge"]["model"], "claude-opus-5-5")       # Claude stays the judge
        o = ctx._backend("generator_other", ctx.cfg["models"]["generator_other"])
        self.assertEqual((o.model, o.extra_sampling), ("google/gemma-4-31B-it", {"top_k": 64}))
        self.assertTrue(o.queue_path.endswith(os.path.join("offline", "queue_generator_other.jsonl")))
        self.assertEqual(ctx.cfg["other_family"]["fraction"], 0.1)

    def test_import_rules(self):
        d = tempfile.mkdtemp()
        try:
            cache = Cache(os.path.join(d, "c.sqlite"))
            queue = os.path.join(d, "q.jsonl")
            b = OfflineBackend("m", "r", queue)
            req = Request(role="generator", stage="reasons", system="s", user="u", schema={}, item="x")
            self.assertTrue(b.enqueue("k1", req))
            self.assertFalse(b.enqueue("k1", req))                        # once per key
            b.enqueue("k2", req)
            ans = os.path.join(d, "a.jsonl")
            with open(ans, "w", encoding="utf8") as fh:
                fh.write(json.dumps({"key": "k1", "data": {"text": "ok"}, "error": "", "finish_reason": "stop"}) + "\n")
                fh.write(json.dumps({"key": "k2", "data": None, "error": "invalid JSON", "finish_reason": "length"}) + "\n")
                fh.write(json.dumps({"key": "k9", "data": {"text": "stray"}}) + "\n")
            n = import_answers(cache, ans, queue)
            self.assertEqual(n, {"imported": 1, "errors": 1, "unknown_keys": 1, "already": 0})
            self.assertEqual(cache.get("k1")["data"], {"text": "ok"})
            self.assertEqual(cache.get("k2")["error"], "invalid JSON")
            self.assertIsNone(cache.get("k9"))
            self.assertEqual(import_answers(cache, ans, queue)["already"], 2)
            self.assertEqual(len(OfflineBackend("m", "r", queue)._queued), 2)   # the queue is read back
            from rrdata.llm import Result
            self.assertTrue(is_pending(Result(error="pending: queued")))
            self.assertFalse(is_pending(Result(error="APIError")))
        finally:
            shutil.rmtree(d)


if __name__ == "__main__":
    unittest.main()
