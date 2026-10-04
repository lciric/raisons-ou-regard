"""The plan of an evaluation: which cue pair frames which scenario, and the list of episodes to run.

**The cue pairs.** Each scenario receives one pair of the framing set (its evaluation text and its deployment text,
written for the same slot), so that its two framings differ by that cue alone. Both variants of a scenario receive
the same pair. A pair goes to a scenario that has a visible place for its slot; pairs are spread over the slots, and
a pair serves once before any pair serves twice. The draw is seeded and recorded.
"""
import random
from collections import defaultdict

from .episode import Condition


def cue_pairs(records):
    """{pair id: {"slot", "eval", "deploy"}} from the framing set's JSONL records (rrdata/cues.py)."""
    pairs = defaultdict(dict)
    for r in records:
        if r.get("set") not in (None, "framing"):
            continue
        p = pairs[r["pair"]]
        p["slot"] = r["slot"]
        p[r["polarity"]] = r
    return {k: v for k, v in pairs.items() if "eval" in v and "deploy" in v}


def assign(scenarios, pairs, seed=0):
    """{scenario pair_id: cue pair id}. Raises if a scenario has no visible place for any available slot."""
    rng = random.Random(seed)
    by_slot = defaultdict(list)
    for pid, p in sorted(pairs.items()):
        by_slot[p["slot"]].append(pid)
    for ids in by_slot.values():
        rng.shuffle(ids)
    uses = defaultdict(int)
    out = {}
    seen = {}
    for scn in sorted(scenarios, key=lambda s: s.id):
        if scn.pair_id in out:
            continue
        slots = sorted(scn.cue_slots(visible_only=True) & set(by_slot))
        if not slots:
            raise ValueError(f"{scn.id}: no visible place for any slot of the framing set")
        seen[scn.pair_id] = slots
        # the least used pair among the scenario's slots; ties broken by the shuffled order
        best = min(((uses[pid], i, pid) for s in slots for i, pid in enumerate(by_slot[s])))
        out[scn.pair_id] = best[2]
        uses[best[2]] += 1
    return out


def episodes_plan(scenarios, pairs, assignment, framings=("evaluation", "deploiement"), slots=("libre", "prerempli"),
                  generations=5, neutral_preface=""):
    """[(scenario, Condition, generation index)] for every scenario, framing, slot and generation."""
    plan = []
    for scn in sorted(scenarios, key=lambda s: s.id):
        pair = pairs[assignment[scn.pair_id]]
        for fr in framings:
            cue = None if fr == "neutre" else pair["eval" if fr == "evaluation" else "deploy"]
            for sl in slots:
                for g in range(generations):
                    plan.append((scn, Condition(framing=fr, slot=sl, cue=cue,
                                                neutral_preface=neutral_preface if sl == "prerempli_neutre" else ""), g))
    return plan
