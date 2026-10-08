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
"""
import json
import os
import re
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


def run(ctx):
    os.environ.setdefault("VLLM_WORKER_MULTIPROC_METHOD", "spawn")
    from huggingface_hub import snapshot_download  # noqa: WPS433
    from vllm import LLM, SamplingParams  # noqa: WPS433

    a = ctx.args
    qpath = a.get("local_queue") or ctx.hub.download(a["queue"], "/workspace/rr/dl")
    queue = read_queue(qpath)
    if not queue:
        raise ValueError("the queue is empty")
    model_id, revision = one_model(queue)
    ctx.progress = f"downloading {model_id}"
    path = a.get("local_model") or snapshot_download(model_id, revision=revision, token=os.environ.get("HF_TOKEN"),
                                                     local_dir="/workspace/rr/models/generator",
                                                     allow_patterns=["*.json", "*.safetensors", "*.txt", "*.jinja", "*.model", "tokenizer*"])
    ctx.progress = f"loading {model_id}"
    t0 = time.time()
    llm = LLM(model=str(path), dtype="auto", tensor_parallel_size=int(a.get("tensor_parallel", 1)),
              max_model_len=int(a.get("max_model_len", 16384)), gpu_memory_utilization=float(a.get("gpu_memory_utilization", 0.9)),
              seed=0, **(a.get("engine") or {}))
    load_seconds = time.time() - t0
    tok = llm.get_tokenizer()

    def prompt(q):
        kw = dict(q["sampling"].get("chat_template_kwargs") or {})
        msgs = [{"role": "system", "content": q["system"]}, {"role": "user", "content": q["user"]}]
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, **kw)

    def params(q):
        s = q["sampling"]
        return SamplingParams(temperature=float(s["temperature"]), top_p=float(s["top_p"]), max_tokens=int(s["max_tokens"]),
                              seed=seed_of(q["key"]), **(s.get("extra") or {}), **structured(q["schema"]))

    out_file = ctx.out / "answers.jsonl"
    chunk = int(a.get("chunk", 512))
    n = {"answers": 0, "errors": 0, "input_tokens": 0, "output_tokens": 0, "finish": {}}
    t1 = time.time()
    with open(out_file, "w", encoding="utf8") as fh:
        for i in range(0, len(queue), chunk):
            part = queue[i:i + chunk]
            ctx.progress = f"generating {i + len(part)}/{len(queue)}"
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
            org._upload(ctx, out_file, "out/answers.jsonl")
    try:
        import vllm  # noqa: WPS433
        version = getattr(vllm, "__version__", None)
    except ImportError:
        version = None
    report = {"model": model_id, "revision": revision, "requests": len(queue), **n, "load_seconds": round(load_seconds, 1),
              "generate_seconds": round(time.time() - t1, 1), "vllm": version,
              "stages": {s: sum(q.get("stage") == s for q in queue) for s in sorted({q.get("stage") for q in queue})}}
    with open(ctx.out / "report.json", "w", encoding="utf8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    return report
