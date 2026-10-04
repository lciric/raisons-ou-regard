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
- The controls of the programme's doctrine come with every measure (see analyse()): random directions (the
  specificity null, nothing more), the same extraction with the polarity of the pairs flipped at random (the
  pipeline null), and the prompt length (a cue set whose two sides differ in length can be read by a length direction).
- The activations of every prompt are saved (states.safetensors, half precision; states.json for pairs and lengths), so
  that further analyses run without a GPU.
- The lexical baseline (decision 24, October 3, 2026): a bag of words (rrdata.lexical, naive Bayes) learned on the
  extraction cue texts, read on the cue texts of each held-out set. The instrument's lexical condition: at the layer
  chosen on the validation probe, the probe must separate the validation set better than this baseline, by a margin
  (job argument "lexical_margin", 0 by default: a proposal, to be fixed in the pre-registration).

Job arguments: {"cues": "<name of data/<name>/ in the results repository>", "adapter": optional path of a LoRA checkpoint
in the repository, "contexts_per_pair": 2, "max_rank": 32, "batch": 16, "extract_set": "extraction"}. "local_cues" and
"local_model" replace the downloads in the offline tests.

"extract_set" names the set whose pairs give the subspace: "extraction" for "I am being evaluated"; another set of the
same format for the separate controls of programme v1.5 (part 3): the unrelated contrasts, the stake contrast. Its two
sides keep the field names "eval" and "deploy". The held-out sets (validation, fresh probe) are read when present.
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
    """Residual stream after each decoder layer, at the last prompt token: a float32 tensor [n, layers, width], and the
    prompt lengths in tokens [n]."""
    import torch  # noqa: WPS433
    tok.padding_side = "left"
    outs, lengths = [], []
    for i in range(0, len(conversations), batch):
        enc = tok.apply_chat_template(conversations[i:i + batch], add_generation_prompt=True, return_tensors="pt", padding=True,
                                      return_dict=True).to(device)
        with torch.no_grad():
            hs = model(**enc, output_hidden_states=True).hidden_states
        outs.append(torch.stack([h[:, -1, :] for h in hs[1:]], dim=1).float().cpu())
        lengths.append(enc["attention_mask"].sum(1).cpu())
    return torch.cat(outs, dim=0), torch.cat(lengths, dim=0)


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


def length_residual(scores, lengths):
    """The scores minus their least-squares fit on the prompt length (with an intercept), on the same prompts."""
    import torch  # noqa: WPS433
    y = torch.as_tensor(scores, dtype=torch.float64)
    x = torch.stack([torch.ones_like(y), torch.as_tensor(lengths, dtype=torch.float64)], dim=1)
    coef = torch.linalg.lstsq(x, y[:, None]).solution
    return y - (x @ coef)[:, 0]


def lexical_baseline(cue_texts):
    """cue_texts: {set: (eval texts, deploy texts)}, one text per prompt, aligned with the states. Returns the AUROC, on
    each held-out set, of a naive Bayes learned on the extraction cues (each distinct cue counted once)."""
    _donnees_on_path()
    from rrdata.lexical import NaiveBayes, auroc as lex_auroc  # noqa: WPS433
    ev, de = cue_texts["extraction"]
    ev_u, de_u = sorted(set(ev)), sorted(set(de))
    nb = NaiveBayes().fit(ev_u + de_u, [1] * len(ev_u) + [0] * len(de_u))
    out = {}
    for key, (e, d) in cue_texts.items():
        if key != "extraction":
            out[key] = round(lex_auroc([nb.score(t) for t in list(e) + list(d)], [1] * len(e) + [0] * len(d)), 4)
    return out


def _donnees_on_path():
    import sys  # noqa: WPS433
    root = Path(__file__).resolve().parents[3] / "donnees"
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))


def lexical_condition(metrics, lexical, margin=0.0):
    """The instrument's lexical condition, at the layer chosen on the validation probe (decision 24; provisional)."""
    best = max(metrics, key=lambda m: m.get("auroc_validation_probe", 0))
    probe, lex = best.get("auroc_validation_probe"), lexical.get("validation")
    return {"layer": best["layer"], "probe_auroc": probe, "lexical_auroc": lex, "margin": margin,
            "passed": None if probe is None or lex is None else bool(probe > lex + margin),
            "rule": "provisional (decision 24): the validation probe must beat a bag of words learned on the extraction "
                    "cues; the measure, the margin and the choice of layer are fixed in the pre-registration"}


def analyse(states, lengths, max_rank, seed=0, n_random=200, n_flips=20, ranks=RANKS):
    """The subspaces of the extraction set and their measures on the held-out sets, with the controls of the programme's
    doctrine. states: {set: (eval [n, layers, width], deploy [n, layers, width])}, pair i of eval matching pair i of
    deploy; lengths: {set: (eval [n], deploy [n])}.

    Per layer and held-out set:
    - the AUROC of the first direction (oriented like the mean difference), of the mean difference itself, and of a
      logistic probe trained on the extraction prompts;
    - paired: the share of pairs whose evaluation prompt projects higher than its deployment twin;
    - the specificity null: the 95th percentile, over random unit directions, of max(AUROC, 1 - AUROC) (a random
      direction has no orientation);
    - the pipeline null: the mean difference with the polarity of exactly half the pairs flipped, drawn n_flips times:
      the 95th percentile of max(AUROC, 1 - AUROC). It is a random direction shaped like the differences (activation
      space is not isotropic). The singular subspace itself cannot be nulled this way: flipping the sign of a
      difference leaves the decomposition unchanged, so the subspace does not depend on which side is "evaluation",
      only its orientation does;
    - the length control: the AUROC of the projection once its linear fit on the prompt length is removed.
    The AUROC of the prompt length alone is given per set.
    """
    import torch  # noqa: WPS433
    g = torch.Generator().manual_seed(seed)
    ev, de = states["extraction"]
    diffs = ev - de
    subs = subspaces(diffs, max_rank)
    n = diffs.shape[0]
    null_dirs = []                                  # [n_flips, layers, width]
    for _ in range(n_flips):
        flips = torch.ones(n, dtype=diffs.dtype)
        flips[torch.randperm(n, generator=g)[: n // 2]] = -1.0
        mu = (diffs * flips[:, None, None]).double().mean(0)
        null_dirs.append((mu / mu.norm(dim=-1, keepdim=True).clamp_min(1e-12)).float())
    null_dirs = torch.stack(null_dirs)
    n_layers, width = ev.shape[1], ev.shape[2]
    rand = torch.randn(n_random, width, generator=g)
    rand = rand / rand.norm(dim=1, keepdim=True)
    held = [k for k in states if k != "extraction"]
    lab = {k: [1] * len(states[k][0]) + [0] * len(states[k][1]) for k in held}
    lens = {k: torch.cat([torch.as_tensor(lengths[k][0]), torch.as_tensor(lengths[k][1])]).double() for k in held}
    summary = {"length_auroc": {k: round(auroc(lens[k], lab[k]), 4) for k in held},
               "length_mean_tokens": {k: [round(float(torch.as_tensor(lengths[k][i]).double().mean()), 1) for i in (0, 1)] for k in held}}
    metrics = []
    for l in range(n_layers):
        m = {"layer": l + 1, "singular_values_top5": [round(float(x), 3) for x in subs[l]["singular_values"][:5]],
             "cos_mean_vs_first": round(float(torch.dot(subs[l]["mean_direction"], subs[l]["basis"][0])), 4)}
        probe = logistic_probe(torch.cat([ev[:, l], de[:, l]]), [1] * len(ev) + [0] * len(de))
        d0 = subs[l]["basis"][0]
        for k in held:
            v_ev, v_de = states[k][0][:, l], states[k][1][:, l]
            x, y = torch.cat([v_ev, v_de]), lab[k]
            proj = x @ d0
            m[f"auroc_{k}_direction"] = round(auroc(proj, y), 4)
            m[f"auroc_{k}_mean_direction"] = round(auroc(x @ subs[l]["mean_direction"], y), 4)
            m[f"auroc_{k}_probe"] = round(auroc(probe(x), y), 4)
            if len(v_ev) == len(v_de):
                m[f"paired_{k}_direction"] = round(float((v_ev @ d0 > v_de @ d0).double().mean()), 4)
            r = torch.tensor([auroc(x @ u, y) for u in rand], dtype=torch.float64)
            m[f"auroc_{k}_random_p95"] = round(float(torch.quantile(torch.maximum(r, 1 - r), 0.95)), 4)
            r = torch.tensor([auroc(x @ u, y) for u in null_dirs[:, l]], dtype=torch.float64)
            m[f"auroc_{k}_pipeline_null_p95"] = round(float(torch.quantile(torch.maximum(r, 1 - r), 0.95)), 4)
            m[f"auroc_{k}_direction_length_residual"] = round(auroc(length_residual(proj, lens[k]), y), 4)
        metrics.append(m)
    summary["metrics"] = metrics
    summary["ranks_available"] = [r for r in ranks if r <= max_rank]
    return subs, summary


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
    extract_set = a.get("extract_set", "extraction")

    ctx.progress = "downloading"
    cue_dir = Path(a["local_cues"]) if a.get("local_cues") else None
    if cue_dir is None:
        cue_dir = Path("/workspace/rr/data/cues")
        cue_dir.mkdir(parents=True, exist_ok=True)
        for name in ("contexts.jsonl", f"{extract_set}.jsonl", "validation.jsonl", "fresh_probe.jsonl"):
            try:
                p = ctx.hub.download(f"data/{a['cues']}/cues/{name}", "/workspace/rr/data/dl")
            except Exception:  # noqa: BLE001  (the held-out sets are optional; the two others are not)
                if name in ("contexts.jsonl", f"{extract_set}.jsonl"):
                    raise
                continue
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
    sets, files = {}, {"extraction": cue_dir / f"{extract_set}.jsonl", "validation": cue_dir / "validation.jsonl",
                       "fresh_probe": cue_dir / "fresh_probe.jsonl"}
    for key, f in files.items():
        if f.exists():
            sets[key] = pair_prompts(_read_jsonl(f), contexts, k, seed)
    if "extraction" not in sets:
        raise FileNotFoundError(f"no {extract_set}.jsonl in the cues")
    cue_text = {}
    for key in sets:
        for r in _read_jsonl(files[key]):
            cue_text.setdefault(r["pair"], {})[r["polarity"]] = r["text"]
    texts = {k: ([cue_text[p[0]]["eval"] for p in v], [cue_text[p[0]]["deploy"] for p in v]) for k, v in sets.items()}
    states, lengths = {}, {}
    for key, pairs in sets.items():
        ctx.progress = f"reading {key} ({len(pairs)} pairs)"
        ev, ev_len = last_token_states(model, tok, [p[1] for p in pairs], batch, device)
        de, de_len = last_token_states(model, tok, [p[2] for p in pairs], batch, device)
        states[key], lengths[key] = (ev, de), (ev_len, de_len)
    # The activations themselves, in half precision: further analyses then need no GPU.
    save_file({f"{k}.{pol}": states[k][i].half().contiguous() for k in states for i, pol in enumerate(("eval", "deploy"))},
              str(ctx.out / "states.safetensors"))
    with open(ctx.out / "states.json", "w", encoding="utf8") as fh:
        json.dump({k: {"pairs": [p[0] for p in sets[k]], "tokens_eval": lengths[k][0].tolist(), "tokens_deploy": lengths[k][1].tolist()}
                   for k in sets}, fh)

    ctx.progress = "analysis"
    subs, summary = analyse(states, lengths, max_rank, seed=seed)
    tensors = {}
    for l, s in enumerate(subs):
        tensors[f"layer_{l + 1:02d}.basis"] = s["basis"].contiguous()
        tensors[f"layer_{l + 1:02d}.mean_direction"] = s["mean_direction"].contiguous()
        tensors[f"layer_{l + 1:02d}.singular_values"] = s["singular_values"].contiguous()
    save_file(tensors, str(ctx.out / "eval_subspace.safetensors"))
    ranking = sorted(summary["metrics"], key=lambda m: -m.get("auroc_validation_probe", 0))
    lexical = lexical_baseline(texts)
    summary = {"model": model_id, "adapter": a.get("adapter"), "extract_set": extract_set, "pairs": {k2: len(v) for k2, v in sets.items()},
               "layers": len(subs), "best_layers_by_validation_probe": [m["layer"] for m in ranking[:5]],
               "lexical_baseline": lexical,
               "lexical_condition": lexical_condition(summary["metrics"], lexical, float(a.get("lexical_margin", 0.0))),
               **summary}
    with open(ctx.out / "eval_subspace.json", "w", encoding="utf8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=1)
    return {k2: summary[k2] for k2 in ("model", "adapter", "extract_set", "pairs", "layers", "best_layers_by_validation_probe",
                                       "lexical_baseline", "lexical_condition")}
