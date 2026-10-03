"""A first inhibition of "I am being evaluated" in the organism (programme v1.5, part 4), exploratory, on the choice
half of MBPP test.

The instrument is the main test's: the subspace extracted once on the starting model (an extract_eval run), applied to
the organism (v1.5, part 3: the extraction is made on the starting model, once, and serves every arm). The organism is
the starting model with the documents' adapter merged, then an expert iteration round's adapter merged.

The halves (organisme/moities_mbpp_test.json, drawn before any inhibition measure): this job reads the choice half,
and the test half only with the argument "porte". The test half serves once, at the gate, at the setting chosen on the
choice half.

Without intervention, then for each setting (a set of layers, a rank, a fraction):
- the conditional gap on the tasks of the half, greedy, as the organism job measures it: the share of fully annotated
  answers under an evaluation cue minus under a deployment cue, with the extraction cues kept out of the expert
  iteration (pairs from cue_pairs_for_training on) and with the framing set; and the shares under no cue;
- the degradation on the organism's own greedy answers to neutral requests (teacher forcing): KL, NLL increase, top-1.
Then the comparator of v1.5 (part 7) for the "top" settings that reduce the extraction gap most: subspaces drawn
according to the covariance of the residual stream, outside the space of "I am being evaluated", of free rank (the
smallest multiple of the setting's rank at which every draw, projected entirely, reaches the setting's KL), each at
the fraction that matches that KL; and the gap under each draw.

Exploratory: the gate itself waits for the cue sets v2 (decision 24), at least 100 comparator draws, the separate
controls and the manipulation check. The subspace of extract_eval-20261003-121743-385d was extracted on every pair of
the extraction set, those kept out of the expert iteration included; the framing set is independent of it.

Job arguments: {"sdf_adapter": "runs/<run>/out/sdf_adapter", "ei_adapter": "runs/<run>/out/ei_round<r>/adapter",
"subspace_run": "<extract_eval run>", "cues": "<cue sets name>", "mbpp": "data/mbpp", "half": "choix",
"settings": [{"layers": "all", "rank": 4, "fraction": 1.0}, ...], "framings": [...],
"comparator": {"top": 2, "n_draws": 8, "multiples": [...], "fractions": [...], "framings": [...]}, "batch": 128,
"kl_batch": 24, "max_new_tokens": 512, "n_contexts": 120, "answer_tokens": 128, "seed": 0}. "local_model",
"local_sdf_adapter", "local_ei_adapter", "local_subspace", "local_cues", "local_mbpp", "local_halves" and "device"
replace the downloads in the offline tests.
"""
import json
import os
import statistics
import time
from pathlib import Path

from . import inhibition_degradation as idg
from . import organism as org

HALVES = Path(__file__).resolve().parents[2] / "organisme" / "moities_mbpp_test.json"
FRAMINGS = ("eval_extraction", "deploy_extraction", "eval_framing", "deploy_framing", "none")
SETTINGS = ({"layers": "all", "rank": 1}, {"layers": "all", "rank": 4}, {"layers": "all", "rank": 16},
            {"layers": [4, 5, 6, 7, 8], "rank": 4}, {"layers": [4, 5, 6, 7, 8], "rank": 16})
COMPARATOR = {"top": 2, "n_draws": 8, "multiples": [1, 2, 3, 4, 6, 8], "fractions": [0.1, 0.2, 0.35, 0.5, 0.75, 1.0],
              "framings": ["eval_extraction", "deploy_extraction"]}


def half_tasks(tasks, halves, half, gate=False):
    """The tasks of one half, in MBPP's order. The test half only for the gate."""
    if half not in ("choix", "test"):
        raise ValueError(f"unknown half {half!r}")
    if half == "test" and not gate:
        raise ValueError("the test half serves only the gate (argument porte)")
    ids = set(halves[half])
    out = [t for t in tasks if t["task_id"] in ids]
    if len(out) != len(ids):
        raise ValueError(f"{len(ids) - len(out)} tasks of the half are missing from MBPP test")
    return out


def setting_key(layers, rank, fraction, n_layers):
    ls = list(layers)
    if ls == list(range(1, n_layers + 1)):
        name = "all"
    elif len(ls) > 1 and ls == list(range(ls[0], ls[-1] + 1)):
        name = f"{ls[0]}-{ls[-1]}"
    else:
        name = "+".join(str(l) for l in ls)
    return f"{name}|r{rank}|f{fraction:g}"


def reduction(base, measured):
    """How much a condition reduces the gaps of the baseline, in points (positive: the gap shrinks)."""
    out = {}
    for name, key in (("extraction", "gap_extraction"), ("framing", "gap_framing")):
        if key in base and key in measured:
            out[name] = round(100.0 * (base[key] - measured[key]), 2)
    return out


def match_fraction(kl_at, points, target, steps=2, tol=0.05):
    """The fraction at which kl_at(fraction) reaches target. The KL grows about as the square of the fraction, so a
    linear interpolation of the KL between two points of a grid lands below the target, and would weaken the comparator;
    the square root of the KL is interpolated instead, then refined by up to `steps` new measures, until the KL is within
    tol (relative) of the target. points: [(fraction, kl)] already measured. Returns (fraction, kl) or (None, None)."""
    import math  # noqa: WPS433
    pts = sorted(points)
    x = k = None
    for _ in range(steps + 1):
        x = idg.interpolate_fraction([(f, math.sqrt(max(v, 0.0))) for f, v in pts], math.sqrt(max(target, 0.0)))
        if x is None:
            return None, None
        k = kl_at(x)
        if abs(k - target) <= tol * target:
            break
        pts = sorted(pts + [(x, k)])
    return x, k


def load_organism(base_path, sdf_dir, ei_dir, dtype, device):
    """The starting model, the documents' adapter merged, then the expert iteration's adapter merged."""
    from peft import PeftModel  # noqa: WPS433
    from transformers import AutoModelForCausalLM  # noqa: WPS433
    model = AutoModelForCausalLM.from_pretrained(base_path, dtype=dtype).to(device)
    model = PeftModel.from_pretrained(model, str(sdf_dir)).merge_and_unload()
    if ei_dir:
        model = PeftModel.from_pretrained(model, str(ei_dir)).merge_and_unload()
    return model.eval()


def run(ctx):
    import torch  # noqa: WPS433
    from huggingface_hub import snapshot_download  # noqa: WPS433
    from safetensors.torch import load_file  # noqa: WPS433
    from transformers import AutoTokenizer  # noqa: WPS433

    a = ctx.args
    hp = org.load_hp(a.get("hp"))
    device = a.get("device", "cuda")
    dt = getattr(torch, hp["dtype"]) if device == "cuda" else torch.float32
    seed = int(a.get("seed", 0))
    batch, kl_batch = int(a.get("batch", 128)), int(a.get("kl_batch", 24))
    max_new = int(a.get("max_new_tokens", hp["measure"]["max_new_tokens"]))
    framing_names = list(a.get("framings", FRAMINGS))
    comp = {**COMPARATOR, **(a.get("comparator") or {})}
    halves = json.loads(Path(a.get("local_halves") or HALVES).read_text(encoding="utf8"))

    ctx.progress = "downloading"

    def fetch(local_key, remote, name):
        if a.get(local_key):
            return str(Path(a[local_key]) / name) if Path(a[local_key]).is_dir() else a[local_key]
        return ctx.hub.download(remote, "/workspace/rr/dl")

    def fetch_dir(local_key, remote):
        if a.get(local_key):
            return Path(a[local_key])
        if not remote:
            raise ValueError(f"no {local_key[len('local_'):]} given")
        return Path(ctx.hub.snapshot([remote.rstrip("/") + "/*"], "/workspace/rr/adapters")) / remote

    base = a.get("local_model") or snapshot_download(hp["base_model"], token=os.environ.get("HF_TOKEN"), local_dir="/workspace/rr/models/base",
                                                     allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
    sdf_dir = fetch_dir("local_sdf_adapter", a.get("sdf_adapter"))
    # without an expert iteration adapter, the organism after the documents only (v1.5: graduate the known case)
    ei_dir = fetch_dir("local_ei_adapter", a.get("ei_adapter")) if (a.get("ei_adapter") or a.get("local_ei_adapter")) else None
    subspace = load_file(fetch("local_subspace", f"runs/{a.get('subspace_run')}/out/eval_subspace.safetensors", "eval_subspace.safetensors"))
    ext = org._read_jsonl(fetch("local_cues", f"data/{a.get('cues')}/cues/extraction.jsonl", "extraction.jsonl"))
    fra = org._read_jsonl(fetch("local_cues", f"data/{a.get('cues')}/cues/framing.jsonl", "framing.jsonl"))
    cfile = fetch("local_cues", f"data/{a.get('cues')}/cues/contexts.jsonl", "contexts.jsonl")
    mb = a.get("mbpp", "data/mbpp")
    tasks = half_tasks(org._read_jsonl(fetch("local_mbpp", f"{mb}/mbpp_test.jsonl", "mbpp_test.jsonl")), halves,
                       a.get("half", "choix"), gate=bool(a.get("porte")))
    ext_split = org.split_cues(ext, int(hp["ei"]["cue_pairs_for_training"]))
    fra_split = org.split_cues(fra, 0)
    all_framings = {"eval_extraction": ext_split["eval"][1], "deploy_extraction": ext_split["deploy"][1],
                    "eval_framing": fra_split["eval"][1], "deploy_framing": fra_split["deploy"][1], "none": [None]}
    framings = {k: all_framings[k] for k in framing_names}
    comp_framings = {k: all_framings[k] for k in comp["framings"]}

    ctx.progress = "loading the organism"
    tok = AutoTokenizer.from_pretrained(base)
    if tok.pad_token is None:
        tok.pad_token = next((t for t in ("<|finetune_right_pad_id|>",) if t in tok.get_vocab()), tok.eos_token)
    model = load_organism(base, sdf_dir, ei_dir, dt, device)
    n_layers, width = model.config.num_hidden_layers, model.config.hidden_size
    max_rank = subspace["layer_01.basis"].shape[0]
    settings = []
    for s in a.get("settings", SETTINGS):
        ls = list(range(1, n_layers + 1)) if s["layers"] == "all" else [int(x) for x in s["layers"]]
        r, f = int(s["rank"]), float(s.get("fraction", a.get("fraction", 1.0)))
        if r > max_rank:
            raise ValueError(f"rank {r} above the subspace's {max_rank}")
        settings.append((setting_key(ls, r, f, n_layers), ls, r, f))

    results = {"organism": {"base": hp["base_model"], "sdf_adapter": a.get("sdf_adapter"), "ei_adapter": a.get("ei_adapter")},
               "subspace_run": a.get("subspace_run"), "cues": a.get("cues"), "half": a.get("half", "choix"), "tasks": len(tasks),
               "framings": {k: len(v) for k, v in framings.items()}, "max_new_tokens": max_new, "settings": {}, "comparator": {}}

    def save(name, rows, line):
        with open(ctx.out / f"measure_{name}.jsonl", "w", encoding="utf8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(ctx.out / "results.json", "w", encoding="utf8") as fh:
            json.dump(results, fh, ensure_ascii=False, indent=1)
        ctx.progress = line
        try:
            ctx.upload_file(ctx.out / "results.json", "out/results.json")
        except Exception as e:  # noqa: BLE001  (a missed interim upload must not stop the job)
            print(f"[rrexp] interim upload failed: {type(e).__name__}", flush=True)

    def gap_line(name, m):
        return (f"{name}: annotated under evaluation {m.get('eval_extraction', {}).get('hinted')}, under deployment "
                f"{m.get('deploy_extraction', {}).get('hinted')}, gap {m.get('gap_extraction')} (framing set: {m.get('gap_framing')})")

    def measure(name, fr):
        t0 = time.time()
        summ, rows = org.measure(model, tok, tasks, fr, batch, max_new, progress=lambda msg: setattr(ctx, "progress", f"{name}: {msg}"))
        summ["seconds"] = round(time.time() - t0, 1)
        return summ, rows

    # 1. the reference answers of the organism, the clean pass and the covariances
    ctx.progress = "reference answers"
    texts, prompts, answers = idg.reference_answers(model, tok, cfile, int(a.get("n_contexts", 120)), int(a.get("answer_tokens", 128)),
                                                    kl_batch, device, ctx.out / "reference_answers.jsonl")
    batches = idg.teacher_batches(tok, prompts, answers, kl_batch, device)
    all_layers = sorted({l for _, ls, _, _ in settings for l in ls})
    ctx.progress = "clean pass"
    clean, covs = idg.clean_pass(model, batches, all_layers)
    results["reference"] = {"contexts": len(texts), "answer_tokens_mean": round(sum(len(x) for x in answers) / max(1, len(answers)), 1)}

    # 2. without intervention
    base_m, rows = measure("baseline", framings)
    results["baseline"] = base_m
    save("baseline", rows, gap_line("baseline", base_m))

    # 3. the inhibition, setting by setting
    def eval_bases(ls, r):
        return {l: subspace[f"layer_{l:02d}.basis"][:r].to(device=device, dtype=dt) for l in ls}

    for key, ls, r, f in settings:
        ctx.progress = f"{key}: degradation"
        pj = idg.Projector(model, eval_bases(ls, r), f)
        with pj:
            deg = idg.degradation(model, batches, clean, pj)
        deg["removed_norm"] = sum(pj.mean_removed().values()) / len(ls)
        with idg.Projector(model, eval_bases(ls, r), f):
            m, rows = measure(key, framings)
        results["settings"][key] = {"layers": ls, "rank": r, "fraction": f, "degradation": deg, "measure": m,
                                    "reduction": reduction(base_m, m)}
        save(key.replace("|", "_"), rows, gap_line(key, m))

    # 4. the comparator, for the settings that reduce the extraction gap most
    order = sorted(settings, key=lambda s: -results["settings"][s[0]]["reduction"].get("extraction", float("-inf")))
    g = torch.Generator().manual_seed(seed)
    sqrt_cache = {}
    for key, ls, r, f in order[:int(comp["top"])]:
        ctx.progress = f"{key}: comparator rank"
        for l in ls:
            if l not in sqrt_cache:
                sqrt_cache[l] = idg.sqrt_outside(covs[l], subspace[f"layer_{l:02d}.basis"].float().to(covs[l].device)).cpu()
        inh = results["settings"][key]["degradation"]
        target = inh["kl"]
        chosen, draws, tried = None, None, []
        for mult in comp["multiples"]:
            rr = r * int(mult)
            if rr > width:
                break
            cand = [{l: idg.covariance_draw(sqrt_cache[l], rr, g) for l in ls} for _ in range(int(comp["n_draws"]))]
            kls = []
            for d in cand:
                with idg.Projector(model, {l: b.to(device=device, dtype=dt) for l, b in d.items()}, 1.0) as pj:
                    kls.append(idg.degradation(model, batches, clean, pj)["kl"])
            tried.append({"multiple": int(mult), "rank": rr, "kl_min": round(min(kls), 5), "kl_median": round(statistics.median(kls), 5)})
            if min(kls) >= target:
                chosen, draws = int(mult), cand
                break
        entry = {"target_kl": round(target, 5), "multiple": chosen, "rank": r * chosen if chosen else None, "tried": tried, "draws": []}
        results["comparator"][key] = entry
        if chosen is None:
            save(f"comparator_{key.replace('|', '_')}_none", [], f"{key}: no comparator rank reaches the inhibition's KL")
            continue
        grid = sorted(float(x) for x in comp["fractions"])
        for i, d in enumerate(draws):
            ctx.progress = f"{key}: comparator draw {i + 1}/{len(draws)}"
            dd = {l: b.to(device=device, dtype=dt) for l, b in d.items()}
            pts = []
            for x in grid:
                with idg.Projector(model, dd, x) as pj:
                    pts.append((x, idg.degradation(model, batches, clean, pj)["kl"]))
            last = {}

            def kl_at(x, dd=dd, last=last):
                pj = idg.Projector(model, dd, x)
                with pj:
                    last["degradation"] = idg.degradation(model, batches, clean, pj)
                last["removed"] = sum(pj.mean_removed().values()) / len(ls)
                return last["degradation"]["kl"]

            x, _ = match_fraction(kl_at, pts, target)
            rec = {"draw": i, "curve": [(round(p, 3), round(k, 5)) for p, k in pts], "fraction": round(x, 4) if x is not None else None}
            if x is not None:
                rec["degradation"] = last["degradation"]
                rec["energy_ratio"] = round(last["removed"] / inh["removed_norm"], 3) if inh.get("removed_norm") else None
                with idg.Projector(model, dd, x):
                    m, rows = measure(f"{key} comparator {i + 1}", comp_framings)
                rec["measure"] = m
                rec["reduction"] = reduction(base_m, m)
            entry["draws"].append(rec)
            save(f"comparator_{key.replace('|', '_')}_{i:02d}", rows if x is not None else [],
                 f"{key}: comparator draw {i + 1}/{len(draws)}, extraction gap reduced by {rec.get('reduction', {}).get('extraction')} points")
        red = [d["reduction"]["extraction"] for d in entry["draws"] if "reduction" in d and "extraction" in d["reduction"]]
        if red:
            entry["summary"] = {"draws_measured": len(red), "reduction_median": round(statistics.median(red), 2),
                                "reduction_max": round(max(red), 2),
                                "inhibition_reduction": results["settings"][key]["reduction"].get("extraction"),
                                "draws_reducing_at_least_as_much": sum(1 for x in red if x >= results["settings"][key]["reduction"].get("extraction", 0))}
    with open(ctx.out / "results.json", "w", encoding="utf8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=1)
    return {"baseline": {k: base_m.get(k) for k in ("gap_extraction", "gap_framing")},
            "settings": {k: {"kl": round(v["degradation"]["kl"], 5), "reduction": v["reduction"]} for k, v in results["settings"].items()},
            "comparator": {k: v.get("summary") for k, v in results["comparator"].items()}}
