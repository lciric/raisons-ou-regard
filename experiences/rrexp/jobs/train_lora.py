"""The SFT by LoRA of the arms of the reasons test (programme v1.4, part 3).

One machine trains several (arm, seed) pairs, one per GPU at a time, from the same downloaded model and data:
- the data are the arm files of the pipeline (arms/<arm>.jsonl), sent beforehand to the results repository under
  data/<dataset>/arms/;
- the hyperparameters are the same in every arm (experiences/hyperparametres_sft.yaml);
- the loss is computed on the last assistant turn only, end-of-turn token included: the situation, the earlier tool
  calls and their results are context;
- an example longer than max_seq_len stops the training: a target is never truncated, and no item is dropped from a
  single arm;
- checkpoints (LoRA adapters only) are saved at equally spaced steps and uploaded to runs/<run_id>/out/<arm>_s<seed>/.

Job arguments: {"dataset": "<name>", "runs": [{"arm": "reasons", "seed": 1}, ...], "hp": {optional overrides}}.
"""
import hashlib
import json
import math
import os
import random
import subprocess
import sys
import time
from pathlib import Path

import yaml

HP_FILE = Path(__file__).resolve().parents[2] / "hyperparametres_sft.yaml"
ARMS = ("actions_only", "neutral_text", "other_reasoning", "generic_principles", "reasons", "reflection")   # programme v1.5, partie 3


def load_hp(overrides=None):
    with open(HP_FILE, encoding="utf8") as fh:
        hp = yaml.safe_load(fh)
    for k, v in (overrides or {}).items():
        node = hp
        *path, last = k.split(".")
        for p in path:
            node = node[p]
        node[last] = v
    return hp


# ---------------------------------------------------------------- data

def tokenize_example(tok, messages, loss="last"):
    """Token ids and labels of one chat example: labels are -100 everywhere but on the last assistant turn, or, with
    loss="assistant_all", on every assistant turn (the reflection arm of programme v1.5: the action, then the reasons
    given after it, in answer to a question of reflection).

    The prefix of each trained turn (the messages before it, then the assistant header) must be a prefix of the full
    rendering; otherwise the chat template does not render that turn as a suffix, and the mask would be wrong.
    """
    if not messages or messages[-1]["role"] != "assistant":
        raise ValueError("the last message of an example must be the assistant turn")
    if loss not in ("last", "assistant_all"):
        raise ValueError(f"unknown loss {loss!r}")
    full = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=False, return_dict=True)["input_ids"]
    turns = [len(messages) - 1] if loss == "last" else [j for j, m in enumerate(messages) if m["role"] == "assistant"]
    labels = [-100] * len(full)
    for j in turns:
        prefix = tok.apply_chat_template(messages[:j], tokenize=True, add_generation_prompt=True, return_dict=True)["input_ids"]
        upto = full if j == len(messages) - 1 else tok.apply_chat_template(messages[:j + 1], tokenize=True, add_generation_prompt=False,
                                                                              return_dict=True)["input_ids"]
        if full[:len(prefix)] != prefix or full[:len(upto)] != upto:
            raise ValueError("the chat template does not render an assistant turn as a suffix of its prompt")
        if len(upto) == len(prefix):
            raise ValueError("empty assistant turn")
        labels[len(prefix):len(upto)] = full[len(prefix):len(upto)]
    return {"input_ids": full, "labels": labels}


def build_examples(tok, records, max_len):
    out = []
    for r in records:
        ex = tokenize_example(tok, r["messages"], r.get("loss", "last"))
        if len(ex["input_ids"]) > max_len:
            raise ValueError(f"example {r['id']} has {len(ex['input_ids'])} tokens > max_seq_len {max_len}: raise max_seq_len for every arm")
        ex["id"] = r["id"]
        out.append(ex)
    return out


def collate(batch, pad_id):
    import torch  # noqa: WPS433
    n = max(len(b["input_ids"]) for b in batch)
    ids = torch.full((len(batch), n), pad_id, dtype=torch.long)
    labels = torch.full((len(batch), n), -100, dtype=torch.long)
    att = torch.zeros((len(batch), n), dtype=torch.long)
    for i, b in enumerate(batch):
        k = len(b["input_ids"])
        ids[i, :k] = torch.tensor(b["input_ids"])
        labels[i, :k] = torch.tensor(b["labels"])
        att[i, :k] = 1
    return {"input_ids": ids, "labels": labels, "attention_mask": att}


def epoch_order(n, seed, epoch):
    rng = random.Random(f"{seed}:{epoch}")
    order = list(range(n))
    rng.shuffle(order)
    return order


def checkpoint_steps(total, k):
    """k steps, equally spaced, the last one at the end."""
    return sorted({max(1, int(round(total * j / k))) for j in range(1, k + 1)})


# ---------------------------------------------------------------- training

def train(model, tok, examples, hp, seed, out_dir, device="cuda", progress=None, upload=None):
    """Trains the LoRA adapters of model on examples. Returns a summary. model already carries the adapters."""
    import torch  # noqa: WPS433
    from transformers import get_cosine_schedule_with_warmup  # noqa: WPS433

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    eff, micro = hp["batch"]["effective"], hp["batch"]["micro"]
    if eff % micro:
        raise ValueError("the effective batch must be a multiple of the micro batch")
    accum = eff // micro
    steps_per_epoch = math.ceil(len(examples) / eff)
    total = steps_per_epoch * hp["schedule"]["epochs"]
    params = [p for p in model.parameters() if p.requires_grad]
    o = hp["optimizer"]
    opt = torch.optim.AdamW(params, lr=o["lr"], betas=tuple(o["betas"]), weight_decay=o["weight_decay"])
    sched = get_cosine_schedule_with_warmup(opt, int(round(hp["schedule"]["warmup_ratio"] * total)), total)
    ckpts = checkpoint_steps(total, hp["checkpoints"])
    pad_id = tok.pad_token_id
    model.train()
    step, log, t0 = 0, [], time.time()
    logf = open(out_dir / "train_log.jsonl", "w", encoding="utf8")
    for epoch in range(hp["schedule"]["epochs"]):
        order = epoch_order(len(examples), seed, epoch)
        for s in range(steps_per_epoch):
            idx = order[s * eff:(s + 1) * eff]
            if not idx:
                continue
            batch = [examples[i] for i in idx]
            n_tokens = sum(sum(1 for l in b["labels"] if l != -100) for b in batch)
            loss_sum = 0.0
            for m in range(0, len(batch), micro):
                mb = collate(batch[m:m + micro], pad_id)
                mb = {k: v.to(device) for k, v in mb.items()}
                logits = model(input_ids=mb["input_ids"], attention_mask=mb["attention_mask"]).logits.float()
                shift_logits, shift_labels = logits[:, :-1, :], mb["labels"][:, 1:]
                loss = torch.nn.functional.cross_entropy(shift_logits.reshape(-1, shift_logits.size(-1)), shift_labels.reshape(-1),
                                                         ignore_index=-100, reduction="sum") / n_tokens
                loss.backward()
                loss_sum += loss.item()
            gnorm = torch.nn.utils.clip_grad_norm_(params, o["max_grad_norm"])
            opt.step()
            sched.step()
            opt.zero_grad(set_to_none=True)
            step += 1
            rec = {"step": step, "epoch": epoch, "loss": round(loss_sum, 5), "grad_norm": round(float(gnorm), 4),
                   "lr": sched.get_last_lr()[0], "tokens": n_tokens, "seconds": round(time.time() - t0, 1)}
            log.append(rec)
            if step % hp.get("log_every", 10) == 0 or step == total:
                logf.write(json.dumps(rec) + "\n")
                logf.flush()
                if progress:
                    progress(f"step {step}/{total} loss {loss_sum:.4f}")
            if step in ckpts:
                cdir = out_dir / "checkpoints" / f"step_{step:05d}"
                model.save_pretrained(cdir)
                if upload:
                    upload(cdir)
    logf.close()
    first = sum(r["loss"] for r in log[:10]) / max(1, len(log[:10]))
    last = sum(r["loss"] for r in log[-10:]) / max(1, len(log[-10:]))
    return {"steps": total, "checkpoints": ckpts, "examples": len(examples), "loss_first_10": round(first, 5), "loss_last_10": round(last, 5),
            "label_tokens": sum(sum(1 for l in e["labels"] if l != -100) for e in examples), "seconds": round(time.time() - t0, 1)}


def build_model(path, hp, device="cuda", dtype=None):
    import torch  # noqa: WPS433
    from peft import LoraConfig, get_peft_model  # noqa: WPS433
    from transformers import AutoModelForCausalLM  # noqa: WPS433
    dt = dtype or getattr(torch, hp["dtype"])
    model = AutoModelForCausalLM.from_pretrained(path, dtype=dt).to(device)
    if hp.get("gradient_checkpointing"):
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
        model.enable_input_require_grads()
    l = hp["lora"]
    cfg = LoraConfig(r=l["r"], lora_alpha=l["alpha"], lora_dropout=l["dropout"], target_modules=l["target_modules"],
                     bias="none", task_type="CAUSAL_LM")
    return get_peft_model(model, cfg)


def train_one(model_path, data_path, arm, seed, hp, out_dir, device="cuda", progress=None, upload=None):
    """One (arm, seed) training, from a local model and a local arm file."""
    import torch  # noqa: WPS433
    from transformers import AutoTokenizer  # noqa: WPS433
    random.seed(seed)
    torch.manual_seed(seed)
    tok = AutoTokenizer.from_pretrained(model_path)
    if tok.pad_token is None:
        tok.pad_token = next((t for t in ("<|finetune_right_pad_id|>",) if t in tok.get_vocab()), tok.eos_token)
    with open(data_path, encoding="utf8") as fh:
        records = [json.loads(l) for l in fh if l.strip()]
    if any(r.get("arm") not in (None, arm) for r in records):
        raise ValueError(f"{data_path} holds examples of another arm than {arm}")
    examples = build_examples(tok, records, hp["max_seq_len"])
    model = build_model(model_path, hp, device=device)
    summary = train(model, tok, examples, hp, seed, out_dir, device=device, progress=progress, upload=upload)
    with open(data_path, "rb") as fh:
        summary["data_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    summary.update(arm=arm, seed=seed, items=len(records), trainable_parameters=sum(p.numel() for p in model.parameters() if p.requires_grad))
    with open(Path(out_dir) / "summary.json", "w", encoding="utf8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=1)
    return summary


# ---------------------------------------------------------------- the job

def _worker(spec_json):
    """Entry point of one training process, pinned to one GPU by CUDA_VISIBLE_DEVICES."""
    spec = json.loads(spec_json)
    from rrexp.hub import Hub  # noqa: WPS433
    hub = Hub()

    def upload(cdir):
        rel = os.path.relpath(cdir, spec["out_root"])
        hub.put_folder(f"runs/{spec['run_id']}/out/{rel}", cdir, f"checkpoint {rel}")

    def progress(msg):
        with open(Path(spec["out_dir"]) / "progress.txt", "w", encoding="utf8") as fh:
            fh.write(msg)

    train_one(spec["model_path"], spec["data_path"], spec["arm"], spec["seed"], spec["hp"], spec["out_dir"], progress=progress, upload=upload)


def run(ctx):
    import torch  # noqa: WPS433
    from huggingface_hub import snapshot_download  # noqa: WPS433

    a = ctx.args
    hp = load_hp(a.get("hp"))
    runs = a["runs"]
    for r in runs:
        if r["arm"] not in ARMS:
            raise ValueError(f"unknown arm {r['arm']}")
    ctx.progress = "downloading the model and the data"
    model_path = snapshot_download(hp["base_model"], token=os.environ.get("HF_TOKEN"), local_dir="/workspace/rr/models/base",
                                   allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
    data = {}
    for arm in sorted({r["arm"] for r in runs}):
        data[arm] = ctx.hub.download(f"data/{a['dataset']}/arms/{arm}.jsonl", "/workspace/rr/data")
    n_gpus = torch.cuda.device_count()
    if n_gpus == 0:
        raise RuntimeError("no GPU visible")
    with open(ctx.out / "hyperparametres.json", "w", encoding="utf8") as fh:
        json.dump(hp, fh, ensure_ascii=False, indent=1)
    queue = list(runs)
    active = {}   # gpu -> (process, run, out_dir)
    results = []
    while queue or active:
        for gpu in range(n_gpus):
            if gpu not in active and queue:
                r = queue.pop(0)
                out_dir = ctx.out / f"{r['arm']}_s{r['seed']}"
                out_dir.mkdir(parents=True, exist_ok=True)
                spec = {"run_id": ctx.run_id, "model_path": model_path, "data_path": data[r["arm"]], "arm": r["arm"], "seed": r["seed"],
                        "hp": hp, "out_dir": str(out_dir), "out_root": str(ctx.out)}
                env = dict(os.environ, CUDA_VISIBLE_DEVICES=str(gpu))
                log = open(out_dir / "worker.log", "w", encoding="utf8")
                p = subprocess.Popen([sys.executable, "-m", "rrexp.jobs.train_lora", json.dumps(spec)], env=env, stdout=log, stderr=subprocess.STDOUT)
                active[gpu] = (p, r, out_dir)
        time.sleep(15)
        lines = []
        for gpu, (p, r, out_dir) in list(active.items()):
            prog = (out_dir / "progress.txt").read_text(encoding="utf8") if (out_dir / "progress.txt").exists() else "starting"
            lines.append(f"gpu{gpu} {r['arm']}_s{r['seed']}: {prog}")
            if p.poll() is not None:
                ok = p.returncode == 0 and (out_dir / "summary.json").exists()
                summary = json.loads((out_dir / "summary.json").read_text(encoding="utf8")) if ok else None
                results.append({"arm": r["arm"], "seed": r["seed"], "ok": ok, "returncode": p.returncode, "summary": summary})
                del active[gpu]
        ctx.progress = f"{len(results)}/{len(runs)} done; " + "; ".join(lines)
    ctx.self_uploaded += [str((ctx.out / f"{r['arm']}_s{r['seed']}" / "checkpoints").resolve()) for r in runs]
    failed = [r for r in results if not r["ok"]]
    if failed:
        raise RuntimeError(f"{len(failed)} training(s) failed: {[(r['arm'], r['seed'], r['returncode']) for r in failed]} (see worker.log)")
    return {"trainings": results, "dataset": a["dataset"], "gpus": n_gpus}


if __name__ == "__main__":
    _worker(sys.argv[1])
