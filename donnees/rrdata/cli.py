"""Command line: python -m rrdata <stage> [options], run from the donnees/ folder.

Stages, in order: plan, situations, actions, reasons, neutral, assemble, audit, report; "all" runs them in order.
"cues" builds the four disjoint cue sets and the deployment prompt (mini-spec v0.2, §6), in its own run.
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
    raise SystemExit(f"unknown stage {stage}")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="rrdata", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=ORDER + ["all", "agreement", "cues"])
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--mock", action="store_true", help="offline mock instead of the Claude API (tests, dry runs)")
    ap.add_argument("--allow-approx-tokenizer", action="store_true", help="approximate token counts if the tokenizer is unavailable")
    ap.add_argument("--allow-unchecked", action="store_true", help="write the arms even when a gate is not met (dry runs)")
    ap.add_argument("--limit", type=int, default=None, help="situations: at most this many items per family (pilot)")
    ap.add_argument("--set", action="append", default=[], help="override a config value, e.g. --set sizes.target_per_family=20")
    ap.add_argument("--sheet", help="agreement: the filled audit sheet")
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
