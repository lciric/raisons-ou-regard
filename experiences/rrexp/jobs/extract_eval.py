"""The representation "I am being evaluated", extracted layer by layer (programme v1.4, part 3, the instruments).

- Contrastive pairs: the same neutral context, preceded by the evaluation cue or by the deployment cue of a pair of
  the extraction set (one cue pair is used with several contexts).
- The residual stream is read at the last token of the prompt, after the assistant header: where the answer starts.
- At each layer, the differences of activation between the two prompts of each pair are stacked; their singular
  value decomposition gives an orthonormal subspace at ranks 1 to 32 (the first singular vector, and the normalized
  mean difference, are both kept).
- Layers are chosen on another set, with other mechanisms (the validation set): the AUROC of the extraction direction
  read on the validation prompts, and the AUROC of a logistic probe trained on the extraction prompts. The fresh-probe
  set (implicit marks of construction) is read the same way, as an exploratory measure.

Job arguments: {"cues": "<name of data/<name>/ in the results repository>", "adapter": optional path of a LoRA checkpoint
in the repository, "contexts_per_pair": 2, "max_rank": 32, "batch": 16}. "local_cues" and "local_model" replace the
downloads in the offline tests.
"""
import json
import os
import random
from pathlib import Path

RANKS = (1, 2, 4, 8, 16, 32)


def _read_jsonl(path):
    with open(path, encoding="utf8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def pair_prompts(cue_recs, contexts, k, seed):
    """[(pair_id, eval_messages, deploy_messages)] for one set. Snippets go before k contexts; rewrites stand alone."""
    pairs = {}
    for r in cue_recs:
        pairs.setdefault(r["pair"], {})[r["polarity"]] = r
    rng = random.Random(seed)
    out = []
    for pid in sorted(pairs):
        p = pairs[pid]
        if set(p) != {"eval", "deploy"}:
            continue
        slot = p["eval"]["slot"]
        if slot == "whole_context":
            out.append((pid, [{"role": "user", "content": p["eval"]["text"]}], [{"role": "user", "content": p["deploy"]["text"]}]))
            continue
        for c in rng.sample(contexts, min(k, len(contexts))):
            def msgs(cue):
                if slot == "system_prompt":
                    return [{"role": "system", "content": cue}, {"role": "user", "content": c}]
                return [{"role": "user", "content": cue + "\n\n" + c}]
            out.append((pid, msgs(p["eval"]["text"]), msgs(p["deploy"]["text"])))
    return out


def last_token_states(model, tok, conversations, batch, device):
    """Residual stream after each decoder layer, at the last prompt token: a float32 tensor [n, layers, width]."""
    import torch  # noqa: WPS433
    tok.padding_side = "left"
    outs = []
    for i in range(0, len(conversations), batch):
        enc = tok.apply_chat_template(conversations[i:i + batch], add_generation_prompt=True, return_tensors="pt", padding=True,
                                      return_dict=True).to(device)
        with torch.no_grad():
            hs = model(**enc, output_hidden_states=True).hidden_states
        outs.append(torch.stack([h[:, -1, :] for h in hs[1:]], dim=1).float().cpu())
    return torch.cat(outs, dim=0)


def auroc(scores, labels):
    """Area under the ROC curve, by ranks (Mann-Whitney), ties counted half."""
    import torch  # noqa: WPS433
    scores, labels = torch.as_tensor(scores, dtype=torch.float64), torch.as_tensor(labels, dtype=torch.bool)
    pos, neg = scores[labels], scores[~labels]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    greater = (pos[:, None] > neg[None, :]).double().sum()
    ties = (pos[:, None] == neg[None, :]).double().sum()
    return float((greater + 0.5 * ties) / (len(pos) * len(neg)))


def subspaces(diffs, max_rank):
    """diffs [n, layers, width] -> per layer: orthonormal basis [r, width] (right singular vectors), singular values,
    normalized mean difference."""
    import torch  # noqa: WPS433
    out = []
    for l in range(diffs.shape[1]):
        d = diffs[:, l, :].double()
        _, s, vh = torch.linalg.svd(d, full_matrices=False)
        r = min(max_rank, vh.shape[0])
        mean = d.mean(0)
        mean = mean / mean.norm().clamp_min(1e-12)
        basis = vh[:r]
        if torch.dot(basis[0], mean) < 0:  # orient the first direction like the mean difference
            basis = basis.clone()
            basis[0] = -basis[0]
        out.append({"basis": basis.float(), "singular_values": s[:r].float(), "mean_direction": mean.float()})
    return out


def logistic_probe(x_train, y_train, steps=300, l2=1e-2):
    """A logistic regression on standardized features, by LBFGS. Returns a scoring function."""
    import torch  # noqa: WPS433
    mu, sd = x_train.mean(0), x_train.std(0).clamp_min(1e-6)
    x = ((x_train - mu) / sd).double()
    y = torch.as_tensor(y_train, dtype=torch.float64)
    w = torch.zeros(x.shape[1], dtype=torch.float64, requires_grad=True)
    b = torch.zeros(1, dtype=torch.float64, requires_grad=True)
    opt = torch.optim.LBFGS([w, b], max_iter=steps, line_search_fn="strong_wolfe")

    def closure():
        opt.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(x @ w + b, y) + l2 * (w * w).sum()
        loss.backward()
        return loss

    opt.step(closure)
    w, b = w.detach(), b.detach()
    return lambda z: (((z - mu) / sd).double() @ w + b)


def run(ctx):
    import torch  # noqa: WPS433
    from huggingface_hub import snapshot_download  # noqa: WPS433
    from safetensors.torch import save_file  # noqa: WPS433
    from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: WPS433

    a = ctx.args
    device = a.get("device", "cuda")
    model_id = a.get("model", "meta-llama/Llama-3.1-8B-Instruct")
    k, max_rank, batch, seed = int(a.get("contexts_per_pair", 2)), int(a.get("max_rank", 32)), int(a.get("batch", 16)), int(a.get("seed", 0))

    ctx.progress = "downloading"
    cue_dir = Path(a["local_cues"]) if a.get("local_cues") else None
    if cue_dir is None:
        cue_dir = Path("/workspace/rr/data/cues")
        for name in ("contexts.jsonl", "extraction.jsonl", "validation.jsonl", "fresh_probe.jsonl"):
            p = ctx.hub.download(f"data/{a['cues']}/cues/{name}", "/workspace/rr/data/dl")
            cue_dir.mkdir(parents=True, exist_ok=True)
            os.replace(p, cue_dir / name)
    path = a.get("local_model") or snapshot_download(model_id, token=os.environ.get("HF_TOKEN"), local_dir="/workspace/rr/models/base",
                                                     allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
    tok = AutoTokenizer.from_pretrained(path)
    if tok.pad_token is None:
        tok.pad_token = next((t for t in ("<|finetune_right_pad_id|>",) if t in tok.get_vocab()), tok.eos_token)
    model = AutoModelForCausalLM.from_pretrained(path, dtype=torch.bfloat16 if device == "cuda" else torch.float32).to(device)
    if a.get("adapter"):
        from peft import PeftModel  # noqa: WPS433
        local = a.get("local_adapter") or ctx.hub.snapshot([a["adapter"].rstrip("/") + "/*"], "/workspace/rr/adapters")
        adir = Path(local) / a["adapter"] if not a.get("local_adapter") else Path(local)
        model = PeftModel.from_pretrained(model, str(adir)).merge_and_unload()
    model.eval()

    contexts = [c["text"] for c in _read_jsonl(cue_dir / "contexts.jsonl") if c["use"] == "snippet"]
    sets = {}
    for key in ("extraction", "validation", "fresh_probe"):
        f = cue_dir / f"{key}.jsonl"
        if f.exists():
            sets[key] = pair_prompts(_read_jsonl(f), contexts, k, seed)
    states = {}
    for key, pairs in sets.items():
        ctx.progress = f"reading {key} ({len(pairs)} pairs)"
        ev = last_token_states(model, tok, [p[1] for p in pairs], batch, device)
        de = last_token_states(model, tok, [p[2] for p in pairs], batch, device)
        states[key] = (ev, de)

    ev, de = states["extraction"]
    subs = subspaces(ev - de, max_rank)
    n_layers = ev.shape[1]
    metrics = []
    for l in range(n_layers):
        m = {"layer": l + 1, "singular_values_top5": [round(float(x), 3) for x in subs[l]["singular_values"][:5]],
             "cos_mean_vs_first": round(float(torch.dot(subs[l]["mean_direction"], subs[l]["basis"][0])), 4)}
        x_train = torch.cat([ev[:, l], de[:, l]])
        y_train = [1] * len(ev) + [0] * len(de)
        probe = logistic_probe(x_train, y_train)
        for key in ("validation", "fresh_probe"):
            if key not in states:
                continue
            v_ev, v_de = states[key]
            x = torch.cat([v_ev[:, l], v_de[:, l]])
            y = [1] * len(v_ev) + [0] * len(v_de)
            m[f"auroc_{key}_direction"] = round(auroc(x @ subs[l]["basis"][0], y), 4)
            m[f"auroc_{key}_probe"] = round(auroc(probe(x), y), 4)
        metrics.append(m)
        ctx.progress = f"layer {l + 1}/{n_layers}"
    tensors = {}
    for l, s in enumerate(subs):
        tensors[f"layer_{l + 1:02d}.basis"] = s["basis"].contiguous()
        tensors[f"layer_{l + 1:02d}.mean_direction"] = s["mean_direction"].contiguous()
        tensors[f"layer_{l + 1:02d}.singular_values"] = s["singular_values"].contiguous()
    save_file(tensors, str(ctx.out / "eval_subspace.safetensors"))
    ranking = sorted(metrics, key=lambda m: -m.get("auroc_validation_probe", 0))
    summary = {"model": model_id, "adapter": a.get("adapter"), "pairs": {k2: len(v) for k2, v in sets.items()},
               "layers": n_layers, "ranks_available": [r for r in RANKS if r <= max_rank],
               "best_layers_by_validation_probe": [m["layer"] for m in ranking[:5]], "metrics": metrics}
    with open(ctx.out / "eval_subspace.json", "w", encoding="utf8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=1)
    return {k2: summary[k2] for k2 in ("model", "adapter", "pairs", "layers", "best_layers_by_validation_probe")}
