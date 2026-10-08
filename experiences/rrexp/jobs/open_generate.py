"""The open generator of the arms' data (decision 37, 8 October 2026): the requests that the data pipeline queued for
it, answered in one run with vLLM, under decoding guided by each request's JSON schema.

Claude's conditions of use forbid taking its outputs as training targets without Anthropic's written permission
(claude/RELECTURES_PARTIE_11_2026-10-08.md): the arms' training targets are written by an open model, and Claude stays a
judge. The pipeline (donnees/, models.generator.backend: offline) queues the requests its cache cannot answer;
"python -m rrdata offline-status" writes those still waiting, and "python -m rrexp send-queue <name> <file>" sends
them to data/<name>/queue.jsonl in the results repository. This job answers them. "python -m rrdata offline-import
--answers <file>" then puts the answers into the pipeline's cache, and its next pass goes on.

Every request carries its model, revision and sampling, which enter the pipeline's cache key: the job refuses a queue
that names several models or revisions. Each answer is drawn with its own seed, taken from the request's key: the same
queue gives the same answers on the same card and software. Reasoning blocks, if a model writes any, are left out of
the answer before its JSON is read.

Job arguments: {"queue": "data/<name>/queue.jsonl", "tensor_parallel": 1, "max_model_len": 16384,
"gpu_memory_utilization": 0.9, "chunk": 512, "engine": {other keyword arguments of vllm.LLM, for instance
{"limit_mm_per_prompt": {"image": 0, "video": 0}} for a multimodal model read as text only}}. The sampling of each
request (temperature, top-p, and the model card's extras: top_k, min_p, presence_penalty...) comes with it.
"local_model" and "local_queue" replace the downloads in the offline tests.
Outputs: out/answers.jsonl ({"key", "data", "error", "finish_reason", "usage"}), sent as each chunk ends, and
out/report.json.

The serve mode (decision 42, 8 October 2026: one rental for the whole pilot). With "serve": true, the job downloads a
model once and answers the queues the session sends, one after the other, while the judges run in the session: each
pass of a stage no longer rents a machine and downloads 127 GB again (vast.ai bills the bandwidth). The session puts
runs/<run_id>/serve/queue_001.jsonl, queue_002.jsonl... in the results repository; the job answers each into
out/answers_NNN.jsonl, then writes out/report_NNN.json, the sign that the answers are complete. Each model runs in a
worker process of its own (python -m rrexp.jobs.open_generate worker): a queue that names another model ends the worker,
which frees the cards, and starts one for the new model. The job ends when runs/<run_id>/serve/stop exists and every
queue sent is answered, or after "idle_minutes" (30) without a new queue. Further arguments: "poll_seconds" (15); "local_serve" (a folder standing for
runs/<run_id>/serve) and "local_models" ({model: folder}) in the offline tests.
"""
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

from . import organism as org

THINK_RE = re.compile(r"<think>.*?</think>", re.S)


def read_queue(path):
    """The requests of a queue, each once (by key), in the queue's order."""
    out, seen = [], set()
    with open(path, encoding="utf8") as fh:
        for line in fh:
            if line.strip():
                q = json.loads(line)
                if q["key"] not in seen:
                    seen.add(q["key"])
                    out.append(q)
    return out


def one_model(queue):
    """The single (model, revision) of a queue; a queue that names several is refused."""
    pairs = {(q["model"], q["revision"]) for q in queue}
    if len(pairs) != 1:
        raise ValueError(f"the queue names {len(pairs)} models or revisions: {sorted(pairs)[:4]}")
    return next(iter(pairs))


def seed_of(key):
    """A sampling seed from the request's cache key (its first 8 hexadecimal digits)."""
    return int(key[:8], 16)


def parse_answer(text):
    """(data, error): the JSON object of an answer, once any reasoning block is left out."""
    t = THINK_RE.sub("", text or "").strip()
    m = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", t, flags=re.S)
    if m:
        t = m.group(1)
    try:
        data = json.loads(t)
    except json.JSONDecodeError as e:
        return None, f"invalid JSON ({e.msg} at {e.pos})"
    if not isinstance(data, dict):
        return None, "the answer is not a JSON object"
    return data, ""


def structured(schema):
    """vLLM's parameters of JSON-guided decoding, under their current name or the older one."""
    try:
        from vllm.sampling_params import StructuredOutputsParams  # noqa: WPS433
        return {"structured_outputs": StructuredOutputsParams(json=schema)}
    except ImportError:
        from vllm.sampling_params import GuidedDecodingParams  # noqa: WPS433
        return {"guided_decoding": GuidedDecodingParams(json=schema)}


MODEL_FILES = ["*.json", "*.safetensors", "*.txt", "*.jinja", "*.model", "tokenizer*"]


def engine_settings(a):
    return {"tensor_parallel": int(a.get("tensor_parallel", 1)), "max_model_len": int(a.get("max_model_len", 16384)),
            "gpu_memory_utilization": float(a.get("gpu_memory_utilization", 0.9)), "engine": a.get("engine") or {}}


def load_llm(path, settings):
    """vLLM's engine on a model folder: (llm, tokenizer, SamplingParams, load seconds)."""
    os.environ.setdefault("VLLM_WORKER_MULTIPROC_METHOD", "spawn")
    from vllm import LLM, SamplingParams  # noqa: WPS433
    t0 = time.time()
    llm = LLM(model=str(path), dtype="auto", tensor_parallel_size=settings["tensor_parallel"], max_model_len=settings["max_model_len"],
              gpu_memory_utilization=settings["gpu_memory_utilization"], seed=0, **settings["engine"])
    return llm, llm.get_tokenizer(), SamplingParams, time.time() - t0


def answer_queue(llm, tok, SamplingParams, queue, out_file, chunk=512, progress=None, after_chunk=None):
    """Answers the requests of a queue into out_file (JSONL, one answer per request); returns the counts."""
    def prompt(q):
        kw = dict(q["sampling"].get("chat_template_kwargs") or {})
        msgs = [{"role": "system", "content": q["system"]}, {"role": "user", "content": q["user"]}]
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **kw)

    def params(q):
        s = q["sampling"]
        return SamplingParams(temperature=float(s["temperature"]), top_p=float(s["top_p"]), max_tokens=int(s["max_tokens"]),
                              seed=seed_of(q["key"]), **(s.get("extra") or {}), **structured(q["schema"]))

    n = {"answers": 0, "errors": 0, "input_tokens": 0, "output_tokens": 0, "finish": {}}
    t1 = time.time()
    with open(out_file, "w", encoding="utf8") as fh:
        for i in range(0, len(queue), chunk):
            part = queue[i:i + chunk]
            if progress:
                progress(f"generating {i + len(part)}/{len(queue)}")
            outs = llm.generate([prompt(q) for q in part], [params(q) for q in part], use_tqdm=False)
            for q, o in zip(part, outs):
                c = o.outputs[0]
                data, err = parse_answer(c.text)
                usage = {"input": len(o.prompt_token_ids or []), "output": len(c.token_ids or [])}
                fh.write(json.dumps({"key": q["key"], "stage": q.get("stage"), "item": q.get("item"), "data": data, "error": err,
                                     "finish_reason": c.finish_reason or "", "usage": usage}, ensure_ascii=False) + "\n")
                n["answers"] += 1
                n["errors"] += bool(err)
                n["input_tokens"] += usage["input"]
                n["output_tokens"] += usage["output"]
                n["finish"][c.finish_reason or ""] = n["finish"].get(c.finish_reason or "", 0) + 1
            fh.flush()
            if after_chunk:
                after_chunk()
    n["generate_seconds"] = round(time.time() - t1, 1)
    return n


def vllm_version():
    try:
        import vllm  # noqa: WPS433
        return getattr(vllm, "__version__", None)
    except ImportError:
        return None


def stages_of(queue):
    return {s: sum(q.get("stage") == s for q in queue) for s in sorted({str(q.get("stage")) for q in queue})}


def run(ctx):
    a = ctx.args
    if a.get("serve"):
        return serve(ctx, a)
    from huggingface_hub import snapshot_download  # noqa: WPS433
    qpath = a.get("local_queue") or ctx.hub.download(a["queue"], "/workspace/rr/dl")
    queue = read_queue(qpath)
    if not queue:
        raise ValueError("the queue is empty")
    model_id, revision = one_model(queue)
    ctx.progress = f"downloading {model_id}"
    path = a.get("local_model") or snapshot_download(model_id, revision=revision, token=os.environ.get("HF_TOKEN"),
                                                     local_dir="/workspace/rr/models/generator", allow_patterns=MODEL_FILES)
    ctx.progress = f"loading {model_id}"
    llm, tok, SamplingParams, load_seconds = load_llm(path, engine_settings(a))
    out_file = ctx.out / "answers.jsonl"
    n = answer_queue(llm, tok, SamplingParams, queue, out_file, int(a.get("chunk", 512)),
                     progress=lambda m: setattr(ctx, "progress", m), after_chunk=lambda: org._upload(ctx, out_file, "out/answers.jsonl"))
    report = {"model": model_id, "revision": revision, "requests": len(queue), **n, "load_seconds": round(load_seconds, 1),
              "vllm": vllm_version(), "stages": stages_of(queue)}
    with open(ctx.out / "report.json", "w", encoding="utf8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    return report


# ---------------------------------------------------------------- the serve mode (decision 42)

def worker_main():
    """The worker process of the serve mode: loads one model (RR_WORKER_SPEC: {"model_path", "ready", settings...}),
    writes the "ready" file, then answers each request read on its standard input ({"queue", "answers", "done",
    "chunk"}) and writes its "done" file (the counts, or the error). It ends when its input closes."""
    spec = json.loads(os.environ["RR_WORKER_SPEC"])
    llm, tok, SamplingParams, load_seconds = load_llm(spec["model_path"], spec)
    _write_atomic(spec["ready"], {"load_seconds": round(load_seconds, 1), "vllm": vllm_version()})
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        try:
            n = answer_queue(llm, tok, SamplingParams, read_queue(req["queue"]), req["answers"], int(req.get("chunk", 512)))
            _write_atomic(req["done"], n)
        except Exception as e:  # noqa: BLE001
            _write_atomic(req["done"], {"error": f"{type(e).__name__}: {e}"[:2000]})


def _write_atomic(path, obj):
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf8") as fh:
        json.dump(obj, fh, ensure_ascii=False)
    os.replace(tmp, path)


class Worker:
    """A worker process for one model, in a session of its own: closing it frees the cards."""

    def __init__(self, model_path, settings, folder, env=None, wait_seconds=3600, poll=2.0):
        self.folder, self.poll = Path(folder), poll
        self.folder.mkdir(parents=True, exist_ok=True)
        ready = self.folder / "ready.json"
        if ready.exists():
            ready.unlink()
        spec = {"model_path": str(model_path), "ready": str(ready), **settings}
        root = str(Path(__file__).resolve().parents[2])           # the experiences/ folder, for "python -m rrexp..."
        e = dict(os.environ if env is None else env, RR_WORKER_SPEC=json.dumps(spec))
        e["PYTHONPATH"] = root + (os.pathsep + e["PYTHONPATH"] if e.get("PYTHONPATH") else "")
        self.proc = subprocess.Popen([sys.executable, "-m", "rrexp.jobs.open_generate", "worker"], stdin=subprocess.PIPE,
                                     text=True, env=e, cwd=root, start_new_session=True)
        self.info = self._wait(ready, wait_seconds, "loading the model")

    def _wait(self, path, seconds, what):
        t0 = time.time()
        while not Path(path).exists():
            if self.proc.poll() is not None:
                raise RuntimeError(f"the worker died while {what} (exit code {self.proc.returncode})")
            if time.time() - t0 > seconds:
                raise RuntimeError(f"the worker took more than {seconds:.0f} s {what}")
            time.sleep(self.poll)
        with open(path, encoding="utf8") as fh:
            return json.load(fh)

    def answer(self, queue_path, answers_path, chunk=512, wait_seconds=7200):
        done = Path(f"{answers_path}.done.json")
        if done.exists():
            done.unlink()
        self.proc.stdin.write(json.dumps({"queue": str(queue_path), "answers": str(answers_path), "done": str(done), "chunk": chunk}) + "\n")
        self.proc.stdin.flush()
        n = self._wait(done, wait_seconds, "answering a queue")
        if "error" in n:
            raise RuntimeError(f"the worker failed on {queue_path}: {n['error']}")
        return n

    def close(self, grace=120):
        if self.proc.poll() is None:
            try:
                self.proc.stdin.close()
                self.proc.wait(timeout=grace)
            except Exception:  # noqa: BLE001
                for sig in (signal.SIGTERM, signal.SIGKILL):
                    try:
                        os.killpg(self.proc.pid, sig)
                        self.proc.wait(timeout=30)
                        break
                    except Exception:  # noqa: BLE001
                        continue


def serve(ctx, a):
    """Answers the queues the session sends, one after the other (see the module's docstring)."""
    from huggingface_hub import snapshot_download  # noqa: WPS433
    settings = engine_settings(a)
    local = Path(a["local_serve"]) if a.get("local_serve") else None
    remote = f"runs/{ctx.run_id}/serve"

    def exists(name):
        return (local / name).exists() if local else ctx.hub.exists(f"{remote}/{name}")

    def fetch(name):
        return str(local / name) if local else ctx.hub.download(f"{remote}/{name}", "/workspace/rr/dl")

    def model_path(model_id, revision):
        if a.get("local_models"):
            return a["local_models"][model_id]
        ctx.progress = f"downloading {model_id}"
        return snapshot_download(model_id, revision=revision, token=os.environ.get("HF_TOKEN"), allow_patterns=MODEL_FILES,
                                 local_dir=f"/workspace/rr/models/{model_id.replace('/', '__')}")

    def put(path, rel):
        """Sends an output at once, and makes sure it arrived: the session reads the answers once the report exists."""
        if local:       # the offline tests read out/ directly
            return
        for attempt in range(4):
            try:
                ctx.hub.put_file(ctx.run_path(rel), path, patience=900)
                return
            except Exception:  # noqa: BLE001
                if attempt == 3:
                    raise
                time.sleep(30 * (attempt + 1))

    idle, poll = float(a.get("idle_minutes", 30)) * 60, float(a.get("poll_seconds", 15))
    worker, current, n, last = None, None, 1, time.time()
    passes, ended = [], ""
    try:
        while True:
            name = f"queue_{n:03d}.jsonl"
            if not exists(name):      # a queue already sent is answered before a stop is honoured
                if exists("stop"):
                    ended = "stop"
                    break
                if time.time() - last > idle:
                    ended = "idle"
                    break
                ctx.progress = f"waiting for {name} ({(time.time() - last) / 60:.0f} min)"
                time.sleep(poll)
                continue
            queue = read_queue(fetch(name))
            model = one_model(queue)
            rec = {"pass": n, "model": model[0], "revision": model[1], "requests": len(queue), "stages": stages_of(queue)}
            if model != current:
                if worker is not None:
                    worker.close()
                    worker = None
                path = model_path(*model)
                ctx.progress = f"loading {model[0]}"
                worker = Worker(path, settings, ctx.out / "worker")
                current = model
                rec["load_seconds"] = worker.info.get("load_seconds")
                rec["vllm"] = worker.info.get("vllm")
            ctx.progress = f"answering {name}: {len(queue)} requests"
            qlocal = ctx.out / "worker" / name
            qlocal.write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in queue), encoding="utf8")
            answers = ctx.out / f"answers_{n:03d}.jsonl"
            rec.update(worker.answer(qlocal, answers, int(a.get("chunk", 512))))
            put(answers, f"out/answers_{n:03d}.jsonl")
            with open(ctx.out / f"report_{n:03d}.json", "w", encoding="utf8") as fh:
                json.dump(rec, fh, ensure_ascii=False, indent=1)
            put(ctx.out / f"report_{n:03d}.json", f"out/report_{n:03d}.json")    # the sign that the answers are complete
            passes.append(rec)
            n, last = n + 1, time.time()
    finally:
        if worker is not None:
            worker.close()
    report = {"serve": True, "ended": ended, "passes": len(passes),
              "requests": sum(p["requests"] for p in passes), "answers": sum(p.get("answers", 0) for p in passes),
              "errors": sum(p.get("errors", 0) for p in passes), "models": sorted({p["model"] for p in passes}),
              "generate_seconds": round(sum(p.get("generate_seconds", 0.0) for p in passes), 1)}
    with open(ctx.out / "report.json", "w", encoding="utf8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    return report


if __name__ == "__main__":
    if sys.argv[1:] == ["worker"]:
        worker_main()
