"""Can the controls of the inhibition reach the degradation the inhibition causes? (programme v1.4, parts 3 and 7)

Part 7, point 3: for each setting of the inhibition (a rank, a fraction projected), each control is brought to the
same degradation; a control that does not reach it, even projecting everything, makes the setting unmatchable. The
counter-reading of v1.4 expects that random subspaces of the same rank cannot reach it for a projection. This job
measures it on the starting model, before any training, with the subspace of an extract_eval run.

For each set of layers and each rank:
- the inhibition: the subspace of "I am being evaluated" (each layer its own), projected out of the residual stream
  at fractions 0.25, 0.5, 0.75 and 1, at every position, after each chosen layer;
- the random subspaces of the same rank: n_random draws, projected out entirely (the most they can degrade);
- the unrelated sensitive directions: the top principal components of the residual stream on the reference answers,
  outside the space of "I am being evaluated" at the largest rank measured, at the same fractions.
The unrelated contrasts ("the train arrived / left the station") are not in this run: their pairs are not written yet.

The comparator of programme v1.5 (part 7), with the argument "comparator": subspaces drawn according to the covariance
of the residual stream on the answer tokens, outside the space of "I am being evaluated" at the largest rank, of a free
rank: the smallest multiple of the inhibition's rank (among "multiples") at which every draw, projected entirely,
reaches the KL of the inhibition's strongest fraction. At that rank, each draw is measured on a grid of fractions, and
the fraction that matches each fraction of the inhibition is interpolated, with the energy it removes (the mean norm
of the removed component) against the inhibition's.

The degradation, the part of the composite that needs no judge, on the clean greedy answers of the starting model to
neutral requests (teacher forcing):
- the KL divergence of the next-token distribution, clean against intervened, averaged over the answer tokens;
- the increase of the mean negative log-likelihood of the clean answers;
- the top-1 agreement with the clean model.
The dose in natural units: the mean norm of the removed component on the answer tokens, divided by the natural gap,
the mean norm of the projection of the extraction pair differences on the same subspace, at the same layer.

Job arguments: {"subspace_run": "<extract_eval run id>", "cues": "<cue sets name>", "layer_sets": [[6], [4, 5, 6, 7, 8],
"all"], "ranks": [1, 2, 4, 8, 16, 32], "fractions": [0.25, 0.5, 0.75, 1.0], "n_random": 20, "n_contexts": 120,
"answer_tokens": 128, "batch": 24, "seed": 0, "comparator": {"multiples": [1, 2, 3, 4, 6, 8], "n_draws": 20,
"fractions": [0.1, 0.2, 0.35, 0.5, 0.75, 1.0]} (optional)}. "local_model", "local_subspace" (a folder with eval_subspace.safetensors
and states.safetensors) and "local_cues" replace the downloads in the offline tests.
"""
import json
import os
import random
from pathlib import Path

RANKS = (1, 2, 4, 8, 16, 32)
FRACTIONS = (0.25, 0.5, 0.75, 1.0)


def orthonormal_random(rank, width, generator):
    """A random orthonormal basis [rank, width] (Gaussian, then QR): a uniformly drawn subspace."""
    import torch  # noqa: WPS433
    q, _ = torch.linalg.qr(torch.randn(width, rank, generator=generator, dtype=torch.float64))
    return q.T.float().contiguous()


def sensitive_basis(cov, eval_basis, rank):
    """The top-rank principal directions of a covariance, once the space of eval_basis is projected out of it."""
    import torch  # noqa: WPS433
    c = cov.double()
    b = eval_basis.double()
    p = torch.eye(c.shape[0], dtype=torch.float64, device=c.device) - b.T @ b
    c = p @ c @ p
    vals, vecs = torch.linalg.eigh((c + c.T) / 2)
    return vecs[:, -rank:].flip(1).T.float().contiguous()


def sqrt_outside(cov, eval_basis):
    """The symmetric square root of a covariance, once the space of eval_basis is projected out of it."""
    import torch  # noqa: WPS433
    c = cov.double()
    b = eval_basis.double()
    p = torch.eye(c.shape[0], dtype=torch.float64, device=c.device) - b.T @ b
    c = p @ c @ p
    vals, vecs = torch.linalg.eigh((c + c.T) / 2)
    return ((vecs * vals.clamp(min=0).sqrt()) @ vecs.T).float().contiguous()


def covariance_draw(sqrt_cov, rank, generator):
    """A random orthonormal basis [rank, width] drawn according to a covariance: the span of rank Gaussian vectors of
    that covariance (sqrt_cov: its symmetric square root, from sqrt_outside)."""
    import torch  # noqa: WPS433
    z = torch.randn(sqrt_cov.shape[0], rank, generator=generator, dtype=torch.float64)
    q, _ = torch.linalg.qr(sqrt_cov.double().cpu() @ z)
    return q.T.float().contiguous()


def interpolate_fraction(points, target):
    """The fraction at which a monotone curve of (fraction, kl) points, from (0, 0), reaches target; None if never."""
    pts = [(0.0, 0.0)] + sorted(points)
    for (f0, k0), (f1, k1) in zip(pts, pts[1:]):
        if k0 <= target <= k1 and k1 > k0:
            return f0 + (target - k0) / (k1 - k0) * (f1 - f0)
    return None


class Projector:
    """Forward hooks that remove fraction * (the component on a basis) from the output of chosen decoder layers.

    bases: {layer (1-based, as in hidden_states): [r, width] orthonormal}. While active, it accumulates the mean norm of
    the removed component over the positions where `mask` (set before each forward) is true.

    Caution (transformers 5.18): the hidden_states returned with output_hidden_states=True are recorded by a hook of
    transformers on each decoder layer. When that hook runs before this one, the recorded state of a hooked layer is the
    state before the projection, while everything downstream does see the projection. A reading of the inhibited
    state (the manipulation check) must therefore take the input of the next layer, by a forward pre-hook.
    """

    def __init__(self, model, bases, fraction):
        self.model, self.fraction, self.handles, self.mask = model, float(fraction), [], None
        self.bases = {l: b for l, b in bases.items()}
        self.removed = {l: [0.0, 0] for l in bases}

    def _hook(self, layer):
        b = self.bases[layer]

        def hook(module, args, output):
            h = output[0] if isinstance(output, tuple) else output
            bb = b.to(device=h.device, dtype=h.dtype)
            comp = (h @ bb.T) @ bb
            if self.mask is not None:
                n = comp.float().norm(dim=-1)[self.mask]
                self.removed[layer][0] += float(n.sum()) * self.fraction
                self.removed[layer][1] += int(n.numel())
            h = h - self.fraction * comp
            return (h,) + tuple(output[1:]) if isinstance(output, tuple) else h
        return hook

    def __enter__(self):
        layers = self.model.model.layers
        for l in self.bases:
            self.handles.append(layers[l - 1].register_forward_hook(self._hook(l)))
        return self

    def __exit__(self, *exc):
        for h in self.handles:
            h.remove()
        self.handles = []

    def mean_removed(self):
        return {l: (s / n if n else 0.0) for l, (s, n) in self.removed.items()}


def teacher_batches(tok, prompts, answers, batch, device):
    """Right-padded batches of prompt + answer, with the mask of the positions that predict an answer token."""
    import torch  # noqa: WPS433
    out = []
    for i in range(0, len(prompts), batch):
        seqs, starts = [], []
        for p, a in zip(prompts[i:i + batch], answers[i:i + batch]):
            seqs.append(list(p) + list(a))
            starts.append(len(p))
        width = max(len(s) for s in seqs)
        ids = torch.full((len(seqs), width), tok.pad_token_id, dtype=torch.long)
        att = torch.zeros((len(seqs), width), dtype=torch.long)
        pred = torch.zeros((len(seqs), width), dtype=torch.bool)   # position t predicts token t + 1
        for j, (s, st) in enumerate(zip(seqs, starts)):
            ids[j, :len(s)] = torch.tensor(s)
            att[j, :len(s)] = 1
            pred[j, st - 1:len(s) - 1] = True
        out.append({"input_ids": ids.to(device), "attention_mask": att.to(device), "pred": pred.to(device)})
    return out


def degradation(model, batches, clean, projector=None):
    """KL(clean || intervened), mean NLL increase and top-1 agreement over the answer tokens."""
    import torch  # noqa: WPS433
    kl_sum, dnll_sum, agree, n = 0.0, 0.0, 0, 0
    for bt, cl in zip(batches, clean):
        if projector is not None:
            projector.mask = bt["pred"]
        with torch.no_grad():
            logits = model(input_ids=bt["input_ids"], attention_mask=bt["attention_mask"]).logits
        lp = torch.log_softmax(logits[bt["pred"]].float(), dim=-1)
        clp = cl["logprobs"]
        kl_sum += float((clp.exp() * (clp - lp)).sum())
        dnll_sum += float((cl["nll"] - (-lp.gather(1, cl["targets"][:, None])[:, 0])).neg().sum())
        agree += int((lp.argmax(-1) == cl["argmax"]).sum())
        n += int(lp.shape[0])
    return {"kl": kl_sum / n, "nll_increase": dnll_sum / n, "top1_agreement": agree / n}


def clean_pass(model, batches, layers_for_cov):
    """The clean log-probabilities on the answer tokens (kept on the GPU in float32: about 8 GB for 120 answers of 128
    tokens over Llama's vocabulary), and the covariance of the residual stream over the answer positions at the given
    layers (for the sensitive directions)."""
    import torch  # noqa: WPS433
    clean, cov, mean, count = [], {}, {}, 0
    for bt in batches:
        with torch.no_grad():
            out = model(input_ids=bt["input_ids"], attention_mask=bt["attention_mask"], output_hidden_states=True)
        lp = torch.log_softmax(out.logits[bt["pred"]].float(), dim=-1)
        targets = bt["input_ids"][:, 1:][bt["pred"][:, :-1]]
        clean.append({"logprobs": lp, "argmax": lp.argmax(-1), "targets": targets, "nll": -lp.gather(1, targets[:, None])[:, 0]})
        for l in layers_for_cov:
            x = out.hidden_states[l][bt["pred"]].double()
            cov[l] = cov.get(l, 0) + x.T @ x
            mean[l] = mean.get(l, 0) + x.sum(0)
        count += int(bt["pred"].sum())
    covs = {}
    for l in layers_for_cov:
        mu = mean[l] / count
        covs[l] = (cov[l] / count - torch.outer(mu, mu)).float()
    return clean, covs


def natural_gaps(states, subspace, layers, ranks):
    """The mean norm of the projection of the extraction pair differences on the first r directions, per layer."""
    import torch  # noqa: WPS433
    d = states["extraction.eval"].float() - states["extraction.deploy"].float()
    out = {}
    for l in layers:
        b = subspace[f"layer_{l:02d}.basis"].float()
        x = d[:, l - 1, :]
        out[l] = {r: float((x @ b[:r].T).norm(dim=-1).mean()) for r in ranks if r <= b.shape[0]}
    return out


def matchability(table, n_random):
    """For each inhibition setting: how many random draws reach its KL when projected entirely, and the fraction of the
    sensitive directions that reaches it (linear interpolation; None if even the full projection does not)."""
    rows = []
    for key, s in table.items():
        rand = s["random_full"]
        sens = s["sensitive"]
        for f, inh in sorted(s["inhibition"].items()):
            target = inh["kl"]
            reach = sum(1 for r in rand if r["kl"] >= target)
            frac = interpolate_fraction([(float(ff), v["kl"]) for ff, v in sens.items()], target)
            frac = round(frac, 3) if frac is not None else None
            rows.append({"setting": key, "fraction": float(f), "kl": round(target, 5), "dose_natural": inh.get("dose_natural"),
                         "random_reaching": reach, "random_draws": n_random, "random_matchable": reach == n_random,
                         "random_kl_max": round(max(r["kl"] for r in rand), 5) if rand else None,
                         "sensitive_fraction": frac, "sensitive_matchable": frac is not None})
    return rows


def run(ctx):
    import torch  # noqa: WPS433
    from huggingface_hub import snapshot_download  # noqa: WPS433
    from safetensors.torch import load_file  # noqa: WPS433
    from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: WPS433

    a = ctx.args
    device = a.get("device", "cuda")
    model_id = a.get("model", "meta-llama/Llama-3.1-8B-Instruct")
    ranks = [int(r) for r in a.get("ranks", RANKS)]
    fractions = [float(f) for f in a.get("fractions", FRACTIONS)]
    n_random, n_ctx = int(a.get("n_random", 20)), int(a.get("n_contexts", 120))
    answer_tokens, batch, seed = int(a.get("answer_tokens", 128)), int(a.get("batch", 24)), int(a.get("seed", 0))

    ctx.progress = "downloading"
    if a.get("local_subspace"):
        sdir = Path(a["local_subspace"])
    else:
        sdir = Path("/workspace/rr/subspace")
        for name in ("eval_subspace.safetensors", "states.safetensors", "eval_subspace.json"):
            p = ctx.hub.download(f"runs/{a['subspace_run']}/out/{name}", "/workspace/rr/dl")
            sdir.mkdir(parents=True, exist_ok=True)
            os.replace(p, sdir / name)
    if a.get("local_cues"):
        cfile = Path(a["local_cues"]) / "contexts.jsonl"
    else:
        cfile = Path(ctx.hub.download(f"data/{a['cues']}/cues/contexts.jsonl", "/workspace/rr/dl"))
    subspace = load_file(str(sdir / "eval_subspace.safetensors"))
    states = load_file(str(sdir / "states.safetensors"))
    path = a.get("local_model") or snapshot_download(model_id, token=os.environ.get("HF_TOKEN"), local_dir="/workspace/rr/models/base",
                                                     allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
    tok = AutoTokenizer.from_pretrained(path)
    if tok.pad_token is None:
        tok.pad_token = next((t for t in ("<|finetune_right_pad_id|>",) if t in tok.get_vocab()), tok.eos_token)
    model = AutoModelForCausalLM.from_pretrained(path, dtype=torch.bfloat16 if device == "cuda" else torch.float32).to(device)
    model.eval()
    n_layers = model.config.num_hidden_layers
    width = model.config.hidden_size
    layer_sets = [list(range(1, n_layers + 1)) if ls == "all" else [int(x) for x in ls]
                  for ls in a.get("layer_sets", [[6], [4, 5, 6, 7, 8], "all"])]
    max_rank_sub = subspace["layer_01.basis"].shape[0]
    ranks = [r for r in ranks if r <= max_rank_sub]

    # 1. the reference answers: greedy answers of the starting model to neutral requests
    ctx.progress = "reference answers"
    with open(cfile, encoding="utf8") as fh:
        texts = [json.loads(l)["text"] for l in fh if l.strip()]
    texts = [t for t in texts][:n_ctx]
    convs = [[{"role": "user", "content": t}] for t in texts]
    tok.padding_side = "left"
    prompts, answers = [], []
    for i in range(0, len(convs), batch):
        enc = tok.apply_chat_template(convs[i:i + batch], add_generation_prompt=True, return_tensors="pt", padding=True,
                                      return_dict=True).to(device)
        with torch.no_grad():
            gen = model.generate(**enc, max_new_tokens=answer_tokens, do_sample=False, pad_token_id=tok.pad_token_id)
        for j in range(gen.shape[0]):
            p = enc["input_ids"][j][enc["attention_mask"][j].bool()].tolist()
            ans = gen[j, enc["input_ids"].shape[1]:].tolist()
            ans = [t for t in ans if t != tok.pad_token_id]
            prompts.append(p)
            answers.append(ans)
    with open(ctx.out / "reference_answers.jsonl", "w", encoding="utf8") as fh:
        for t, ans in zip(texts, answers):
            fh.write(json.dumps({"request": t, "answer": tok.decode(ans, skip_special_tokens=True), "tokens": len(ans)}) + "\n")
    batches = teacher_batches(tok, prompts, answers, batch, device)
    all_layers = sorted({l for ls in layer_sets for l in ls})
    ctx.progress = "clean pass"
    clean, covs = clean_pass(model, batches, all_layers)
    gaps = natural_gaps(states, subspace, all_layers, ranks)

    # the sensitive directions of each layer, once: the top ones of the same decomposition serve every rank
    sens_all = {l: sensitive_basis(covs[l], subspace[f"layer_{l:02d}.basis"].float().to(covs[l].device), max(ranks)).cpu()
                for l in all_layers}
    comp = a.get("comparator")
    if comp:
        sqrt_all = {l: sqrt_outside(covs[l], subspace[f"layer_{l:02d}.basis"].float().to(covs[l].device)).cpu() for l in all_layers}
        multiples = [int(m) for m in comp.get("multiples", [1, 2, 3, 4, 6, 8])]
        n_draws = int(comp.get("n_draws", 20))
        grid = [float(f) for f in comp.get("fractions", [0.1, 0.2, 0.35, 0.5, 0.75, 1.0])]
        comparator = {}
    g = torch.Generator().manual_seed(seed)
    table = {}
    for ls in layer_sets:
        key = "all" if len(ls) == n_layers else "+".join(str(l) for l in ls)
        for r in ranks:
            ctx.progress = f"layers {key}, rank {r}"
            ev_b = {l: subspace[f"layer_{l:02d}.basis"][:r].float() for l in ls}
            sens_b = {l: sens_all[l][:r] for l in ls}
            entry = {"layers": ls, "rank": r, "inhibition": {}, "sensitive": {}, "random_full": []}
            for f in fractions:
                pj = Projector(model, ev_b, f)
                with pj:
                    m = degradation(model, batches, clean, pj)
                rem = pj.mean_removed()
                m["dose_natural"] = round(sum(rem[l] / gaps[l][r] for l in ls if gaps[l].get(r)) / len(ls), 4)
                m["removed_norm"] = round(sum(rem.values()) / len(ls), 4)
                entry["inhibition"][f] = m
                ps = Projector(model, sens_b, f)
                with ps:
                    entry["sensitive"][f] = degradation(model, batches, clean, ps)
            for _ in range(n_random):
                rb = {l: orthonormal_random(r, width, g) for l in ls}
                pr = Projector(model, rb, 1.0)
                with pr:
                    entry["random_full"].append(degradation(model, batches, clean, pr))
            table[f"{key}|r{r}"] = entry
            if comp:
                ctx.progress = f"layers {key}, rank {r}: comparator"
                comparator[f"{key}|r{r}"] = comparator_setting(model, batches, clean, entry, ls, r, width, sqrt_all, multiples,
                                                               n_draws, grid, g)
    rows = matchability(table, n_random)
    summary = {"model": model_id, "subspace_run": a.get("subspace_run"), "layer_sets": layer_sets, "ranks": ranks,
               "fractions": fractions, "n_random": n_random, "contexts": len(texts),
               "answer_tokens_mean": round(sum(len(x) for x in answers) / max(1, len(answers)), 1),
               "natural_gaps": {str(l): v for l, v in gaps.items()},
               "settings": {k: {**v, "inhibition": {str(f): m for f, m in v["inhibition"].items()},
                                "sensitive": {str(f): m for f, m in v["sensitive"].items()}} for k, v in table.items()},
               "matchability": rows}
    if comp:
        summary["comparator"] = comparator
    with open(ctx.out / "degradation.json", "w", encoding="utf8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=1)
    n_rand_ok = sum(1 for r in rows if r["random_matchable"])
    out = {"settings": len(rows), "random_matchable": n_rand_ok, "sensitive_matchable": sum(1 for r in rows if r["sensitive_matchable"])}
    if comp:
        out["comparator_matchable"] = sum(1 for c in comparator.values() for f in c["fractions"].values() if f["draws_matched"] == c["n_draws"])
        out["comparator_rank_multiples"] = sorted({c["multiple"] for c in comparator.values() if c["multiple"]})
    return out


def comparator_setting(model, batches, clean, entry, layers, rank, width, sqrt_all, multiples, n_draws, grid, generator):
    """The comparator for one inhibition setting: the smallest rank multiple at which every covariance draw, projected
    entirely, reaches the KL of the inhibition's strongest fraction; then, at that rank, each draw's fraction matching
    each fraction of the inhibition, and the energy it removes against the inhibition's."""
    import statistics  # noqa: WPS433
    inh = entry["inhibition"]
    target_full = max(m["kl"] for m in inh.values())
    chosen, draws, tried = None, None, []
    for m in multiples:
        rr = rank * m
        if rr > width:
            break
        cand = [{l: covariance_draw(sqrt_all[l], rr, generator) for l in layers} for _ in range(n_draws)]
        kls = []
        for d in cand:
            with Projector(model, d, 1.0) as pj:
                kls.append(degradation(model, batches, clean, pj)["kl"])
        tried.append({"multiple": m, "rank": rr, "kl_min": round(min(kls), 5), "kl_median": round(statistics.median(kls), 5)})
        if min(kls) >= target_full:
            chosen, draws = m, cand
            break
    res = {"multiple": chosen, "rank": rank * chosen if chosen else None, "n_draws": n_draws, "tried": tried, "fractions": {}}
    if chosen is None:
        for f, mi in inh.items():
            res["fractions"][str(f)] = {"kl": round(mi["kl"], 5), "draws_matched": 0}
        return res
    curves, norms = [], []
    for d in draws:
        pts, full_norm = [], None
        for f in grid:
            with Projector(model, d, f) as pj:
                k = degradation(model, batches, clean, pj)["kl"]
            pts.append((f, k))
            if f == max(grid):
                full_norm = sum(pj.mean_removed().values()) / len(layers) / f
        curves.append(pts)
        norms.append(full_norm)
    for f, mi in sorted(inh.items()):
        fr = [interpolate_fraction(c, mi["kl"]) for c in curves]
        ok = [(x, n) for x, n in zip(fr, norms) if x is not None]
        ratio = [x * n / mi["removed_norm"] for x, n in ok if mi.get("removed_norm")]
        res["fractions"][str(f)] = {"kl": round(mi["kl"], 5), "draws_matched": len(ok),
                                    "matched_fraction_median": round(statistics.median([x for x, _ in ok]), 3) if ok else None,
                                    "energy_ratio_median": round(statistics.median(ratio), 3) if ratio else None}
    return res
