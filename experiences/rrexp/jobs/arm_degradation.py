"""The output degradation of each trained arm (registration, Appendix B.8: "The trained arms are interventions too.
Reading or choice differences between arms are reported with each arm's output degradation").

The starting model is loaded once; each arm's adapter (the last checkpoint that train_lora writes) is loaded on it in
turn, and the starting model is measured with the adapters disabled:
1. the starting model's greedy answers to the first 120 neutral requests of the cue sets' contexts, the reference answers
   of the matched degradation (Appendix B.1), with their fingerprint, and the clean pass;
2. for each arm, KL(starting model || arm) on those answers, the mean NLL increase and the top-1 agreement;
3. with "composite": the composite (module composite) on the starting model and on each arm, the coherence judged by
   JEV-27B once the models are freed;
4. for each arm, each component against the starting model's value, with the composite's tolerances (composite.check),
   and its shift from the starting model. This is the arm's own degradation, reported beside the differences between
   arms. Nothing here is matched, chosen or decided.

Job arguments: {"training_run": "<train_lora run id>", "runs": [{"arm": "reasons", "seed": 1}, ...],
"cues": "<cue sets name>" (its contexts.jsonl gives the neutral requests), "n_contexts": 120, "answer_tokens": 128,
"kl_batch": 24, "composite": {"items": "items_v1", "judge": true, "batch": 64, "max_new": {component: tokens}}}.
"local_model", "local_adapters" ({"<arm>_s<seed>": adapter folder}), "local_cues", "local_jev", "items_dir" and "device"
replace the downloads in the offline tests.
"""
import gc
import hashlib
import json
import os
from pathlib import Path

from .. import composite as cp
from . import inhibition_degradation as idg
from . import organism as org

ITEMS = Path(__file__).resolve().parents[2] / "composite" / "items_v1"


def last_checkpoint(folder):
    """The last checkpoint of a training run: the step_<n> folder with the largest n."""
    steps = sorted((p for p in Path(folder).glob("step_*") if p.is_dir()), key=lambda p: int(p.name.split("_")[1]))
    if not steps:
        raise FileNotFoundError(f"no checkpoint in {folder}")
    return steps[-1]


def shifts(base, arm, components=cp.COMPONENTS):
    """Each component's shift from the starting model, in its own unit (the perplexity as a share of the starting
    model's)."""
    out = {}
    for c in components:
        if base.get(c) is None or arm.get(c) is None:
            continue
        kind, _ = cp.TOLERANCES[c]
        out[c] = round((arm[c] - base[c]) / base[c], 4) if kind == "rel" else round(arm[c] - base[c], 4)
    return out


def run(ctx):
    import torch  # noqa: WPS433
    from huggingface_hub import snapshot_download  # noqa: WPS433
    from peft import PeftModel  # noqa: WPS433
    from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: WPS433

    a = ctx.args
    hp = org.load_hp(a.get("hp"))
    device = a.get("device", "cuda")
    dt = getattr(torch, hp["dtype"]) if device == "cuda" else torch.float32
    kl_batch = int(a.get("kl_batch", 24))
    runs = [(r["arm"], int(r["seed"])) for r in a.get("runs", [])]
    local_adapters = a.get("local_adapters") or {}
    names = [f"{arm}_s{seed}" for arm, seed in runs] or sorted(local_adapters)
    if not names:
        raise ValueError("no arm to measure: give runs (with training_run) or local_adapters")
    ccfg = a.get("composite")

    ctx.progress = "downloading"
    base = a.get("local_model") or snapshot_download(hp["base_model"], token=os.environ.get("HF_TOKEN"), local_dir="/workspace/rr/models/base",
                                                     allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
    if a.get("local_cues"):
        cfile = str(Path(a["local_cues"]) / "contexts.jsonl")
    else:
        cfile = ctx.hub.download(f"data/{a.get('cues')}/cues/contexts.jsonl", "/workspace/rr/dl")
    adapters = {}
    for name in names:
        if name in local_adapters:
            adapters[name] = Path(local_adapters[name])
        else:
            remote = f"runs/{a['training_run']}/out/{name}/checkpoints"
            adapters[name] = last_checkpoint(Path(ctx.hub.snapshot([remote + "/*"], "/workspace/rr/adapters")) / remote)

    ctx.progress = "loading the starting model"
    tok = AutoTokenizer.from_pretrained(base)
    if tok.pad_token is None:
        tok.pad_token = next((t for t in ("<|finetune_right_pad_id|>",) if t in tok.get_vocab()), tok.eos_token)
    model = AutoModelForCausalLM.from_pretrained(base, dtype=dt).to(device).eval()
    model = PeftModel.from_pretrained(model, str(adapters[names[0]]), adapter_name=names[0])
    for name in names[1:]:
        model.load_adapter(str(adapters[name]), adapter_name=name)
    model.eval()

    results = {"training_run": a.get("training_run"), "arms": {}, "adapters": {n: str(p) for n, p in adapters.items()},
               "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"}

    def save_results(line):
        with open(ctx.out / "results.json", "w", encoding="utf8") as fh:
            json.dump(results, fh, ensure_ascii=False, indent=1)
        ctx.progress = line
        org._upload(ctx, ctx.out / "results.json", "out/results.json")

    # 1. the reference answers of the starting model, and the clean pass
    ctx.progress = "reference answers"
    ref_file = ctx.out / "reference_answers.jsonl"
    with model.disable_adapter():
        texts, prompts, answers = idg.reference_answers(model, tok, cfile, int(a.get("n_contexts", 120)),
                                                        int(a.get("answer_tokens", 128)), kl_batch, device, ref_file)
        batches = idg.teacher_batches(tok, prompts, answers, kl_batch, device)
        clean, _ = idg.clean_pass(model, batches, [])
    org._upload(ctx, ref_file, "out/reference_answers.jsonl")
    results["reference"] = {"contexts": len(texts), "sha256": hashlib.sha256(ref_file.read_bytes()).hexdigest(),
                            "answer_tokens_mean": round(sum(len(x) for x in answers) / max(1, len(answers)), 1)}

    # 2. the KL of each arm
    for name in names:
        model.set_adapter(name)
        ctx.progress = f"{name}: KL"
        results["arms"][name] = {"degradation": {k: round(v, 6) for k, v in idg.degradation(model, batches, clean).items()}}
        save_results(f"{name}: KL {results['arms'][name]['degradation']['kl']:.4f}")
    del clean
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    # 3. the composite, on the starting model then on each arm
    if ccfg:
        items_dir = Path(a.get("items_dir") or ITEMS.parent / ccfg.get("items", ITEMS.name))
        items = cp.load_items(items_dir, ccfg.get("components", cp.COMPONENTS))
        manifest = json.loads((items_dir / "manifest.json").read_text(encoding="utf8"))
        results["composite"] = {"items": {k: {"n": v["n"], "sha256": v["sha256"]} for k, v in manifest["sets"].items() if k in items},
                                "tolerances": {k: list(v) for k, v in cp.TOLERANCES.items()}, "conditions": {}}
        coh_rows = {}

        def composite_here(name):
            vals, rows = cp.measure(model, tok, items, int(ccfg.get("batch", 64)), max_new=ccfg.get("max_new"),
                                    progress=lambda m: setattr(ctx, "progress", f"{name}: {m}"))
            with open(ctx.out / f"composite_{name}.jsonl", "w", encoding="utf8") as fh:
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            org._upload(ctx, ctx.out / f"composite_{name}.jsonl", f"out/composite_{name}.jsonl")
            coh_rows[name] = [r for r in rows if r["component"] == "coherence"]
            results["composite"]["conditions"][name] = vals
            save_results(f"{name}: composite measured")

        with model.disable_adapter():
            composite_here("starting_model")
        for name in names:
            model.set_adapter(name)
            composite_here(name)
        if ccfg.get("judge", True) and any(coh_rows.values()):
            from ..jev import FILES as JEV_FILES, REPO as JEV_REPO, REVISION as JEV_REVISION, Jev  # noqa: WPS433
            ctx.progress = "loading the judge"
            del model
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            jpath = a.get("local_jev") or snapshot_download(JEV_REPO, revision=JEV_REVISION, allow_patterns=JEV_FILES,
                                                            local_dir="/workspace/rr/models/jev27b", token=os.environ.get("HF_TOKEN"))
            jev = Jev(jpath, device=device)
            with open(ctx.out / "composite_coherence_judged.jsonl", "w", encoding="utf8") as fh:
                for name, rows in coh_rows.items():
                    cp.judge_coherence(jev, rows, progress=lambda m, name=name: setattr(ctx, "progress", f"{name}: {m}"))
                    rated = [r["rating"] for r in rows]
                    results["composite"]["conditions"][name]["coherence"] = round(sum(rated) / len(rated), 4) if rated else None
                    for r in rows:
                        fh.write(json.dumps({"condition": name, "id": r["id"], "rating": r["rating"]}, ensure_ascii=False) + "\n")
            org._upload(ctx, ctx.out / "composite_coherence_judged.jsonl", "out/composite_coherence_judged.jsonl")
            results["composite"]["judge"] = {"model": JEV_REPO, "revision": JEV_REVISION}
        # 4. each arm against the starting model
        base_vals = results["composite"]["conditions"]["starting_model"]
        for name in names:
            vals = results["composite"]["conditions"][name]
            results["arms"][name]["composite"] = vals
            results["arms"][name]["shift_from_starting_model"] = shifts(base_vals, vals)
            results["arms"][name]["within_tolerance_of_starting_model"] = cp.check(base_vals, vals)
    save_results("done")
    return {"reference_sha256": results["reference"]["sha256"],
            "arms": {n: {"kl": v["degradation"]["kl"],
                         "within": (v.get("within_tolerance_of_starting_model") or {}).get("within"),
                         "at_fault": (v.get("within_tolerance_of_starting_model") or {}).get("at_fault")}
                     for n, v in results["arms"].items()}}
