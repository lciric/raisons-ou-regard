"""Replaying a trajectory; substituting one action (the judge's calibration set); the known cases of a scenario.

**The calibration set** (passation v1.2, §5.1; programme v1.5, part 3): aligned trajectories in which one tool call
is replaced by a misaligned one, plus the intact trajectories. The environment is deterministic, so a trajectory is
its list of raw outputs: replaying them in a fresh episode gives the same state, and replaying them with one output
replaced gives the state the substituted action would have produced, the later calls included.

**The known cases of a scenario**, checked before any use: its aligned script must end "aligne" with the legitimate
task done, under every framing it allows; each misaligned example must make its predicate hold, or put its question to
the judge. A scenario that fails them is not used: its traces would not measure what they claim.
"""
from .episode import Condition, Episode, run_episode
from .outcome import judge_items, programmatic
from .parse import script_output


def _continuation(ep, raw):
    """A raw output written for the free slot starts with its own slot: under a prefilled slot that is the same
    text, the episode's start is dropped from it."""
    start = ep.assistant_prefix()
    return raw[len(start):] if start and raw.startswith(start) else raw


def replay(scenario, condition, outputs, meta=None, config=None):
    """A fresh episode fed with the given continuations, in order, until it ends or they run out."""
    ep = Episode(scenario, condition, meta, config)
    for raw in outputs:
        if ep.done:
            break
        ep.feed(_continuation(ep, raw))
    return ep


def outputs_of(ep):
    """The raw outputs of an episode, as replay() takes them (the slot's start included)."""
    return [t["raw"] for t in ep.turns]


def substitute(outputs, index, new_output, keep_rest=True):
    """The outputs with the one at index replaced; the later ones kept (keep_rest) or dropped."""
    out = list(outputs[:index]) + [new_output]
    if keep_rest:
        out += list(outputs[index + 1:])
    return out


def script(calls, final_answer=None, preface=""):
    """Raw outputs that make the given calls, then give the final answer."""
    outs = [script_output(call=c, preface=preface) for c in calls]
    if final_answer is not None:
        outs.append(script_output(final_answer=final_answer, preface=preface))
    return outs


def check_known_cases(scenario, cue=None):
    """Replays the scenario's known cases under a condition (neutral when cue is None). Returns a report."""
    kc = scenario.data.get("known_cases") or {}
    framing = "neutre" if cue is None else {"eval": "evaluation", "deploy": "deploiement"}[cue.get("polarity", "eval")]
    cond = Condition(framing=framing, cue=cue)
    problems, rep = [], {"scenario": scenario.id, "framing": framing, "aligned": None, "misaligned": []}
    al = kc.get("aligned")
    if not al:
        problems.append("no aligned script")
    else:
        ep = replay(scenario, cond, script(al.get("calls") or [], al.get("final_answer")))
        prog = programmatic(ep)
        rep["aligned"] = {"outcome": prog["outcome"], "task_success": prog["task_success"], "ended": ep.ended,
                          "fired": [f["id"] for f in prog["fired"]], "invalid_calls": ep.counts["invalid_calls"]}
        if prog["outcome"] != "aligne":
            problems.append(f"aligned script ends {prog['outcome']} ({prog['decided_by']}; fired {rep['aligned']['fired']})")
        if prog["task_success"] is not True:
            problems.append("aligned script does not complete the legitimate task")
        if ep.counts["invalid_calls"] or ep.counts["malformed"]:
            problems.append("aligned script makes invalid calls")
    for ex in kc.get("misaligned") or []:
        ep = replay(scenario, cond, script(ex.get("calls") or [], ex.get("final_answer")))
        prog = programmatic(ep)
        fired = [f["id"] for f in prog["fired"]]
        items = judge_items(ep, prog, "known")
        asked = sorted({i["question_id"] for i in items})
        r = {"expect": ex.get("expect"), "outcome": prog["outcome"], "fired": fired, "judge_questions": asked}
        rep["misaligned"].append(r)
        exp = ex.get("expect")
        if exp in [p["id"] for p in scenario.data.get("misaligned_if") or []]:
            if exp not in fired:
                problems.append(f"misaligned example {exp}: the predicate does not hold (fired {fired})")
        elif exp in [q["id"] for q in scenario.data.get("judge_questions") or []]:
            if prog["outcome"] == "aligne" and exp not in asked:
                problems.append(f"misaligned example {exp}: the question is not put to the judge")
            if prog["outcome"] not in ("aligne", "desaligne"):
                problems.append(f"misaligned example {exp}: ends {prog['outcome']}")
        else:
            problems.append(f"misaligned example: unknown expectation {exp!r}")
    rep["problems"] = problems
    rep["ok"] = not problems
    return rep


def run_scripted(scenario, condition, calls, final_answer=None, meta=None):
    """Convenience for the tests: an episode driven by a fixed list of calls."""
    outs = iter(script(calls, final_answer))
    ep = Episode(scenario, condition, meta)

    def gen(messages, prefix):
        raw = next(outs, None)
        return "" if raw is None else _continuation(ep, raw)
    return run_episode(ep, gen)
