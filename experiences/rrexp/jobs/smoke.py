"""The end-to-end trial of the chain, and the measures the cost estimates need.

What it checks: the machine (GPU, CUDA, packages); the download of Llama-3.1-8B-Instruct with the restricted token;
generation in bf16; whether the model writes a tool call in the programme's format, as the agentic families
describe it in the system prompt (rrdata.render.TOOLS_INTRO); the upload of the outputs.

What it measures: the download and load times; the throughput of sampled generation at temperature 1, as in the
evaluations, at several batch sizes, with Hugging Face generate (the path of the inhibition hooks, without vLLM);
the peak GPU memory.
"""
import json
import os
import sys
import time
from pathlib import Path

MODEL = "meta-llama/Llama-3.1-8B-Instruct"

# Five short agentic tasks, written for this trial only; none comes from the families of the mini-spec.
FORMAT_PROBES = [
    ("You are an operations agent for the reporting team of a regional furniture retailer.",
     "Please produce the September sales summary from /srv/data/sales_2026_09.csv and save it to /srv/reports/sept_summary.txt."),
    ("You are an assistant agent for the facilities office of a mid-sized engineering firm.",
     "Find out which meeting rooms are booked tomorrow morning; the bookings are in /shared/rooms/bookings.txt."),
    ("You are a support agent for a small online bookshop. You work on the ticket queue.",
     "Ticket 4471 says the customer was charged twice. Check the order file /data/orders/88213.json and tell me what you find."),
    ("You are a maintenance agent for the internal wiki of a logistics company.",
     "The page /wiki/onboarding.md has broken links. List them for me first; do not change anything yet."),
    ("You are a data agent for the analytics team of a public library network.",
     "Count the loans recorded in /data/loans/2026-09.csv and send the figure to Ines on the analytics team."),
]


def _programme_format():
    """The tool block of the agentic families, from the data pipeline's code (it travels in the bundle)."""
    root = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(root / "donnees"))
    from rrdata.render import TOOLS_INTRO  # noqa: WPS433
    from rrdata.textutil import parse_tool_calls  # noqa: WPS433
    with open(root / "donnees" / "spec" / "families.json", encoding="utf8") as fh:
        tools = json.load(fh)["tools"]
    names = ["run_shell", "read_file", "write_file", "send_message"]
    block = TOOLS_INTRO + "\n" + "\n".join(f"- {tools[t]['signature']}: {tools[t]['description_en']}" for t in names)
    return block, parse_tool_calls


def _pad_token(tok):
    for t in ("<|finetune_right_pad_id|>", "<|reserved_special_token_0|>"):
        if t in tok.get_vocab():
            return t
    return tok.eos_token


def run(ctx):
    import torch  # noqa: WPS433
    from huggingface_hub import snapshot_download  # noqa: WPS433
    from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: WPS433

    a = ctx.args
    model_id = a.get("model", MODEL)
    batch_sizes = a.get("batch_sizes", [1, 8, 32, 64])
    new_tokens = int(a.get("new_tokens", 256))
    samples = int(a.get("format_samples", 8))
    device = a.get("device", "cuda")
    cuda = device == "cuda"
    out = {"model": model_id}

    ctx.progress = "downloading the model"
    t0 = time.time()
    path = a.get("local_model") or snapshot_download(model_id, token=os.environ.get("HF_TOKEN"),
                                                     local_dir=f"/workspace/rr/models/{model_id.replace('/', '__')}",
                                                     allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
    out["download_seconds"] = round(time.time() - t0, 1)
    out["model_bytes"] = sum(f.stat().st_size for f in Path(path).rglob("*") if f.is_file())

    ctx.progress = "loading the model"
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained(path)
    tok.padding_side = "left"
    tok.pad_token = _pad_token(tok)
    model = AutoModelForCausalLM.from_pretrained(path, dtype=torch.bfloat16 if cuda else torch.float32).to(device)
    model.eval()
    out["load_seconds"] = round(time.time() - t0, 1)
    out["gpu"] = torch.cuda.get_device_name(0) if cuda else "none (cpu)"
    out["pad_token"] = tok.pad_token
    eos = model.generation_config.eos_token_id

    def generate(convs, do_sample, max_new, forced=False):
        enc = tok.apply_chat_template(convs, add_generation_prompt=True, return_tensors="pt", padding=True, return_dict=True).to(device)
        kw = dict(max_new_tokens=max_new, do_sample=do_sample, pad_token_id=tok.pad_token_id, eos_token_id=eos)
        if do_sample:
            kw.update(temperature=1.0, top_p=1.0, top_k=0)
        if forced:
            kw["min_new_tokens"] = max_new
        with torch.no_grad():
            seq = model.generate(**enc, **kw)
        gen = seq[:, enc["input_ids"].shape[1]:]
        return [tok.decode(g, skip_special_tokens=True) for g in gen], enc["input_ids"].shape[1]

    # 1. The tool-call format of the programme
    ctx.progress = "format probes"
    tools_block, parse_tool_calls = _programme_format()
    rows, valid_greedy, valid_sampled, n_sampled = [], 0, 0, 0
    for i, (system, task) in enumerate(FORMAT_PROBES):
        conv = [{"role": "system", "content": system + "\n\n" + tools_block}, {"role": "user", "content": task}]
        texts, _ = generate([conv], do_sample=False, max_new=200)
        texts_s, _ = generate([conv] * samples, do_sample=True, max_new=200)
        for kind, t in [("greedy", texts[0])] + [("sampled", x) for x in texts_s]:
            try:
                calls = parse_tool_calls(t)
                ok = len(calls) == 1
            except ValueError:
                calls, ok = [], False
            if kind == "greedy":
                valid_greedy += ok
            else:
                valid_sampled += ok
                n_sampled += 1
            rows.append({"probe": i, "kind": kind, "valid_single_call": ok, "tool": calls[0]["name"] if ok else None, "text": t})
    with open(ctx.out / "format_probes.jsonl", "w", encoding="utf8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    out["format"] = {"greedy_valid": f"{valid_greedy}/{len(FORMAT_PROBES)}", "sampled_valid": f"{valid_sampled}/{n_sampled}"}

    # 2. Throughput of sampled generation, at forced length
    ctx.progress = "throughput"
    long_user = ("Here is the transcript of a long support conversation that I need summarized for the team lead. " * 12).strip()
    conv = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": long_user}]
    out["throughput"] = []
    for bs in batch_sizes:
        if cuda:
            torch.cuda.synchronize()
            torch.cuda.reset_peak_memory_stats()
        t0 = time.time()
        texts, prompt_len = generate([conv] * bs, do_sample=True, max_new=new_tokens, forced=True)
        if cuda:
            torch.cuda.synchronize()
        dt = time.time() - t0
        out["throughput"].append({"batch": bs, "prompt_tokens": int(prompt_len), "new_tokens": new_tokens, "seconds": round(dt, 2),
                                  "tokens_per_second": round(bs * new_tokens / dt, 1),
                                  "peak_gpu_gb": round(torch.cuda.max_memory_allocated() / 1e9, 2) if cuda else None})
        ctx.progress = f"throughput batch {bs}: {out['throughput'][-1]['tokens_per_second']} tok/s"
    with open(ctx.out / "smoke.json", "w", encoding="utf8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out
