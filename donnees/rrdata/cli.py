"""Command line: python -m rrdata <stage> [options], run from the donnees/ folder.

Stages, in order: plan, situations, actions, reasons, neutral, assemble, audit, report; "all" runs them in order.
"cues" builds the four disjoint cue sets and the deployment prompt (mini-spec v0.2, §6), in its own run.

With an open generator run in batches (decision 37; models.generator.backend: offline), each pass of the stages queues
the requests the cache cannot answer. "offline-status" counts them and writes those still waiting to
offline/waiting_generator.jsonl, for the job open_generate of experiences/; "offline-import --answers <file>" puts its
answers into the cache. The next pass of the stages takes the waiting items up again.
"""
import argparse
import json

from . import assemble as asm
from . import stages
from .context import Context

ORDER = ["plan", "situations", "actions", "reasons", "neutral", "assemble", "audit", "report"]


def run(ctx, stage, args):
    if stage == "plan":
        return {"items": len(stages.plan(ctx))}
    if stage == "situations":
        recs = stages.situations(ctx, limit=args.limit)
        return {"ok": sum(r["status"] == "ok" for r in recs.values()), "total": len(recs)}
    if stage in ("actions", "reasons", "neutral"):
        recs = getattr(stages, stage)(ctx)
        return {"ok": sum(r["status"] == "ok" for r in recs.values()), "total": len(recs)}
    if stage == "assemble":
        return asm.assemble(ctx, allow_unchecked=args.allow_unchecked)
    if stage == "audit":
        return asm.audit(ctx)
    if stage == "report":
        return {"report": asm.report(ctx), "manifest": asm.manifest(ctx)}
    if stage == "agreement":
        return asm.audit_agreement(ctx, args.sheet)
    if stage == "cues":
        from . import cues
        return cues.build(ctx)
    if stage in ("offline-status", "offline-import"):
        return offline(ctx, stage, args)
    raise SystemExit(f"unknown stage {stage}")


def offline(ctx, stage, args):
    """The queue of the open generator: its state and the requests still waiting, or the import of answers."""
    import os  # noqa: WPS433

    from .llm import import_answers  # noqa: WPS433
    b = ctx.llm.backends["generator"]
    if not getattr(b, "offline", False):
        raise SystemExit("the generator of this configuration is not an open model run in batches (models.generator.backend)")
    if stage == "offline-import":
        if not args.answers:
            raise SystemExit("offline-import needs --answers <file>")
        return import_answers(ctx.llm.cache, args.answers, b.queue_path)
    queued = []
    if os.path.exists(b.queue_path):
        with open(b.queue_path, encoding="utf8") as fh:
            queued = [json.loads(l) for l in fh if l.strip()]
    waiting = [q for q in queued if ctx.llm.cache.get(q["key"]) is None]
    path = ctx.path("offline/waiting_generator.jsonl")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf8") as fh:
        for q in waiting:
            fh.write(json.dumps(q, ensure_ascii=False) + "\n")
    return {"queued": len(queued), "answered": len(queued) - len(waiting), "waiting": len(waiting), "waiting_file": path,
            "model": b.model, "revision": b.revision}


def main(argv=None):
    ap = argparse.ArgumentParser(prog="rrdata", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=ORDER + ["all", "agreement", "cues", "offline-status", "offline-import"])
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--mock", action="store_true", help="offline mock instead of the Claude API (tests, dry runs)")
    ap.add_argument("--allow-approx-tokenizer", action="store_true", help="approximate token counts if the tokenizer is unavailable")
    ap.add_argument("--allow-unchecked", action="store_true", help="write the arms even when a gate is not met (dry runs)")
    ap.add_argument("--limit", type=int, default=None, help="situations: at most this many items per family (pilot)")
    ap.add_argument("--set", action="append", default=[], help="override a config value, e.g. --set sizes.target_per_family=20")
    ap.add_argument("--sheet", help="agreement: the filled audit sheet")
    ap.add_argument("--answers", help="offline-import: the answers of the job open_generate (JSONL)")
    args = ap.parse_args(argv)
    overrides = {}
    for kv in args.set:
        k, v = kv.split("=", 1)
        try:
            v = json.loads(v)
        except json.JSONDecodeError:
            pass
        overrides[k] = v
    ctx = Context(args.config, mock=args.mock, allow_approx=args.allow_approx_tokenizer, overrides=overrides)
    for s in (ORDER if args.stage == "all" else [args.stage]):
        print(s, json.dumps(run(ctx, s, args), ensure_ascii=False))
