"""Generation stages: plan, situations, actions, reasons, neutral prefaces.

Each stage reads the records of the previous one, processes the items not yet done, and appends one record
per item to its own JSONL file, so that an interrupted run resumes where it stopped. An item dropped at any
stage is dropped from every arm.
"""
import json
import math
import random

from .render import render_situation, tools_block
from .schemas import (ACTION_SCHEMA, EVAL_SCHEMA, JUDGE_ACTION_SCHEMA, JUDGE_NEUTRAL_SCHEMA, JUDGE_REASONS_SCHEMA,
                      REALISM_SCHEMA, SITUATION_SCHEMA, TEXT_SCHEMA)
from .textutil import (STOPWORDS, eval_awareness_hits, jaccard, parse_tool_calls, shingles, text_outside_tool_calls,
                       word_count)
from .tokens import within

PRINCIPLE_NUMBER_RE = r"\bprinciple\s*(?:no\.?\s*|#\s*)?\d"


# ---------------------------------------------------------------- plan

def plan(ctx):
    """Draws the items of every training family: variation values, variant and contrast flags at exact shares."""
    target = ctx.cfg["sizes"]["target_per_family"]
    n = int(math.ceil(target * ctx.cfg["sizes"]["overprovision"]))
    meta = {"seed": ctx.cfg["seed"], "target_per_family": target, "per_family": n}
    done = ctx.load("plan.jsonl")
    if done:
        with open(ctx.path("plan_meta.json"), encoding="utf8") as fh:
            old = json.load(fh)
        if old != meta:
            raise RuntimeError(f"this run already has a plan for {old}, not {meta}: use another run_name")
        return done
    with open(ctx.path("plan_meta.json"), "w", encoding="utf8") as fh:
        json.dump(meta, fh)
    recs = []
    for fam in ctx.spec.train:
        rng = random.Random(f"{ctx.cfg['seed']}:plan:{fam.key}")
        variant = [None] * n
        pos = 0
        order = list(range(n))
        rng.shuffle(order)
        for v in fam.variants:
            k = int(round(v["share"] * n))
            for i in order[pos:pos + k]:
                variant[i] = v["key"]
            pos += k
        contrast = [False] * n
        order = list(range(n))
        rng.shuffle(order)
        for i in order[:int(round(fam.data["contrast_share"] * n))]:
            contrast[i] = True
        axes = fam.data["variation_axes"]
        for i in range(n):
            var = {}
            for axis, values in axes.items():
                if axis == "indicator" and variant[i] != "indicator":
                    continue
                var[axis] = rng.choice(values)
            cp = None
            if contrast[i]:
                cp = rng.choice(ctx.spec.contrast_principles(fam.key, variant[i]))
            recs.append({"id": f"{fam.key}-{i:04d}", "family": fam.key, "index": i, "variant": variant[i],
                         "contrast": contrast[i], "contrast_principle": cp, "variation": var})
    ctx.write("plan.jsonl", recs)
    return {r["id"]: r for r in recs}


# ---------------------------------------------------------------- situations

def _situation_system(ctx, fam):
    d = fam.data
    if d["format"] == "agentic":
        tools = ", ".join(d["tools"])
        fmt = ("An agentic transcript. The assistant is an agent that acts through tools; the pipeline adds the description of the "
               "tools to the system prompt, so do not describe them. Each assistant turn is exactly one tool call, written as "
               '<tool_call>{"name": "<tool>", "arguments": {...}}</tool_call>, optionally preceded by one short sentence. '
               f"Each tool turn is the result of the call just before it. Available tools: {tools}.")
    else:
        fmt = "A chat between a user and the assistant. No tool turns."
    block = ctx.fill("situation_system", description=d["description_en"], aligned=d["aligned_en"],
                     misaligned=" ".join(d["misaligned_en"]), trap=d["trap_en"], excluded=d["excluded_en"], format_block=fmt,
                     system_prompt_guidance=d["system_prompt_guidance_en"], turns_guidance=d["turns_guidance_en"],
                     required_facts=", ".join(d["required_facts"]), expected=d["expected_strings_en"],
                     forbidden=d["forbidden_patterns_en"])
    return ctx.generator_system(block)


def _situation_user(ctx, fam, item):
    var = "Variation: " + "; ".join(f"{k} = {v}" for k, v in item["variation"].items()) + "."
    variant = ""
    for v in fam.variants:
        if v["key"] == item["variant"]:
            variant = "Variant: " + v["description_en"]
    if item["contrast"]:
        p = ctx.spec.principles[item["contrast_principle"]]
        contrast = ("CONTRAST SITUATION. Build the situation with this change, everything else being as usual for the family: "
                    f"{p.off_edit_en} Because of this change, the aligned next action is the most direct one: "
                    f"{fam.data['contrast_aligned_en']} Write aligned_behavior and misaligned_behaviors accordingly: here, "
                    "a needless refusal or needless caution is misaligned.")
    else:
        contrast = "The usual dilemma of the family fully applies: the aligned next action is the one described for the family."
    return ctx.fill("situation_user", variation=var, variant=variant, contrast=contrast)


def check_situation(ctx, fam, sit):
    """Structural and lexical checks of a generated situation. Returns a list of problems."""
    probs = []
    d = fam.data
    turns = sit.get("turns") or []
    if not turns:
        return ["no turns"]
    if turns[0]["role"] != "user":
        probs.append("first turn is not a user turn")
    if turns[-1]["role"] == "assistant":
        probs.append("last turn is an assistant turn")
    names = {f["name"] for f in sit.get("facts", [])}
    missing = [n for n in d["required_facts"] if n not in names]
    if missing:
        probs.append(f"missing facts {missing}")
    if d["format"] == "agentic":
        allowed = set(d["tools"])
        prev = None
        for t in turns:
            if t["role"] == "assistant":
                try:
                    calls = parse_tool_calls(t["content"])
                except ValueError as e:
                    probs.append(f"bad tool call: {e}")
                    continue
                if len(calls) != 1:
                    probs.append("an assistant turn does not hold exactly one tool call")
                elif calls[0]["name"] not in allowed:
                    probs.append(f"unknown tool {calls[0]['name']}")
            if t["role"] == "tool" and prev != "assistant":
                probs.append("a tool turn does not follow an assistant turn")
            prev = t["role"]
        if not sit.get("forbidden_patterns"):
            probs.append("no forbidden pattern")
    else:
        if any(t["role"] == "tool" for t in turns):
            probs.append("tool turn in a chat situation")
        if any("<tool_call>" in t["content"] for t in turns):
            probs.append("tool call in a chat situation")
    if fam.key == "pushback":
        if len(sit.get("expected_strings", [])) != 1 or len(sit.get("forbidden_patterns", [])) != 1:
            probs.append("pushback needs exactly one expected string and one forbidden pattern")
    for s in sit.get("forbidden_patterns", []) + sit.get("expected_strings", []):
        if len(s.strip()) < 2 or s.strip().lower() in STOPWORDS:
            probs.append(f"pattern too weak: {s!r}")
    exp = sit.get("expected_strings", [])
    forb = sit.get("forbidden_patterns", [])
    for e in exp:
        for f in forb:
            if f.strip() and f.strip().lower() in e.lower():
                probs.append(f"forbidden pattern {f!r} is inside expected string {e!r}")
    full = render_situation(sit, tools_block(ctx.spec, fam))
    everything = full + "\n" + "\n".join([sit.get("decision_point", ""), sit.get("aligned_behavior", "")] +
                                          sit.get("misaligned_behaviors", []) + [f["value"] for f in sit.get("facts", [])])
    res = ctx.reserved.find(everything)
    if res:
        probs.append(f"reserved words {res}")
    ev = eval_awareness_hits(full)
    if ev:
        probs.append(f"evaluation-awareness wording {ev}")
    return probs


def situations(ctx, limit=None):
    items = plan(ctx)
    done = ctx.load("situations.jsonl")
    todo = [it for it in items.values() if _retry(done, it["id"])]
    if limit:
        keep = {}
        for it in sorted(items.values(), key=lambda r: r["index"]):
            keep.setdefault(it["family"], [])
            if len(keep[it["family"]]) < limit:
                keep[it["family"]].append(it["id"])
        allowed = {i for ids in keep.values() for i in ids}
        todo = [it for it in todo if it["id"] in allowed]
    systems = {fam.key: _situation_system(ctx, fam) for fam in ctx.spec.train}
    max_att = ctx.cfg["attempts"]["situation"]

    def one(item):
        fam = ctx.spec.families[item["family"]]
        user = _situation_user(ctx, fam, item)
        rec = dict(item, status="dropped", reason="", situation=None, attempts=0, problems=[])
        for a in range(max_att):
            rec["attempts"] = a + 1
            r = ctx.llm.call(_req(ctx, "generator", "situation", systems[fam.key], user, SITUATION_SCHEMA, a, item["id"],
                                  {"family": fam.key, "format": fam.data["format"], "required_facts": fam.data["required_facts"]}))
            if r.refusal:
                rec["reason"] = "refusal:situation"
                break
            if r.error:
                rec["problems"].append(r.error)
                continue
            probs = check_situation(ctx, fam, r.data)
            if probs:
                rec["problems"].append(probs)
                continue
            rec["situation"] = r.data
            rec["status"], rec["reason"] = "ok", ""
            break
        else:
            rec["reason"] = "error:api" if _api_only(rec["problems"]) else "checks:situation"
        if rec["status"] == "ok":
            j = ctx.llm.call(_req(ctx, "judge", "judge_realism", ctx.judge_system(ctx.prompt("judge_realism_system")),
                                  ctx.fill("judge_realism_user", situation=render_situation(rec["situation"], tools_block(ctx.spec, fam))),
                                  REALISM_SCHEMA, 0, item["id"], {}))
            rec["realism"] = j.data if (j.data and not j.refusal) else {"refusal": j.refusal, "error": j.error}
        ctx.append("situations.jsonl", rec)
        return rec

    ctx.parallel(one, todo)
    return _dedup(ctx)


def _dedup(ctx):
    """Drops near-duplicate situations inside a family (Jaccard of word 5-gram shingles)."""
    recs = ctx.load("situations.jsonl")
    thr = ctx.cfg["dedup_jaccard"]
    by_fam = {}
    for r in sorted(recs.values(), key=lambda r: r["index"]):
        if r["status"] == "ok":
            by_fam.setdefault(r["family"], []).append(r)
    changed = False
    for fam_recs in by_fam.values():
        kept = []
        for r in fam_recs:
            sh = shingles(render_situation(r["situation"]))
            dup = next((k for k, ksh in kept if jaccard(sh, ksh) > thr), None)
            if dup:
                r["status"], r["reason"], r["duplicate_of"] = "dropped", "duplicate", dup
                changed = True
            else:
                kept.append((r["id"], sh))
    if changed:
        ctx.write("situations.jsonl", sorted(recs.values(), key=lambda r: (r["family"], r["index"])))
    return recs


# ---------------------------------------------------------------- shared helpers

def _req(ctx, role, stage, system, user, schema, sample, item, meta):
    from .llm import Request
    return Request(role=role, stage=stage, system=system, user=user, schema=schema, sample=sample, item=item, meta=meta)


def _situation_text(ctx, rec):
    fam = ctx.spec.families[rec["family"]]
    return render_situation(rec["situation"], tools_block(ctx.spec, fam))


def _avoid_words(ctx, situation_text):
    """Token-set words and value words to keep out of an action or a neutral preface.

    With admit_token_set_words_from_situation (a proposal, see PIPELINE_DONNEES), a word the situation already
    uses is admitted; otherwise every such word is kept out.
    """
    allw = [e for e, _ in ctx.avoidable.entries]
    if ctx.cfg.get("admit_token_set_words_from_situation", True):
        present = ctx.avoidable.present(situation_text)
        return [w for w in allw if w not in present]
    return allw


def _eval_judge(ctx, text, item, label):
    r = ctx.llm.call(_req(ctx, "judge", "judge_eval_awareness", ctx.judge_system(ctx.prompt("judge_eval_awareness_system")),
                          ctx.fill("judge_eval_awareness_user", text=text), EVAL_SCHEMA, 0, f"{item}:{label}", {}))
    if r.refusal or r.error or r.data is None:
        return None, r
    return bool(r.data.get("eval_awareness")), r


def _constraints(expected=(), forbidden=(), avoid=(), feedback="", previous=""):
    lines = []
    if expected:
        lines.append("The turn must contain these exact strings: " + "; ".join(repr(e) for e in expected) + ".")
    if forbidden:
        lines.append("It must not contain these strings: " + "; ".join(repr(f) for f in forbidden) + ".")
    if avoid:
        lines.append("Do not use these words, in any form: " + ", ".join(avoid) + ".")
    if feedback:
        lines.append("YOUR PREVIOUS ATTEMPT WAS REJECTED. Previous attempt:\n" + previous + "\nReasons: " + feedback + "\nWrite a new one.")
    return ("\n" + "\n".join(lines)) if lines else ""


def _retry(done, key):
    """An item is to do again when its last record failed on API errors only (network, credit, overload): such a
    failure says nothing about the item. A refusal or a failed check is final."""
    return key not in done or done[key].get("reason") == "error:api"


def _api_only(attempts):
    """True when every attempt of an item ended on an API error."""
    return bool(attempts) and all((isinstance(a, str)) or (isinstance(a, dict) and set(a) == {"error"}) for a in attempts)


def _ok_ids(*maps):
    ids = None
    for m in maps:
        s = {k for k, r in m.items() if r.get("status") == "ok"}
        ids = s if ids is None else ids & s
    return ids or set()


# ---------------------------------------------------------------- actions

def _action_system(ctx, fam):
    d = fam.data
    if d["format"] == "agentic":
        tools = "; ".join(ctx.spec.tools[t]["signature"] for t in d["tools"])
        rule = ("- It is exactly one tool call, written as <tool_call>{\"name\": \"<tool>\", \"arguments\": {...}}</tool_call>, "
                "optionally preceded by one short sentence. Messages to colleagues go through send_message. "
                f"Available tools: {tools}.")
    else:
        rule = "- It is an ordinary chat reply, without markup."
    return ctx.generator_system(ctx.fill("action_system", max_words=d["action_max_words"], format_rule=rule))


def check_action(ctx, fam, rec, action, avoid):
    probs = []
    sit = rec["situation"]
    low = action.lower()
    for e in sit.get("expected_strings", []):
        if e.lower() not in low:
            probs.append(f"missing expected string {e!r}")
    for f in sit.get("forbidden_patterns", []):
        if f.lower() in low:
            probs.append(f"contains forbidden string {f!r}")
    prose = text_outside_tool_calls(action) if fam.data["format"] == "agentic" else action
    used = [w for w in ctx.avoidable.find(action) if w in avoid]
    if used:
        probs.append(f"uses words to avoid {used}")
    res = ctx.reserved.find(action)
    if res:
        probs.append(f"reserved words {res}")
    ev = eval_awareness_hits(action)
    if ev:
        probs.append(f"evaluation-awareness wording {ev}")
    n = word_count(action)
    if n > fam.data["action_max_words"]:
        probs.append(f"too long ({n} words > {fam.data['action_max_words']})")
    if fam.data["format"] == "agentic":
        try:
            calls = parse_tool_calls(action)
        except ValueError as e:
            return probs + [f"bad tool call: {e}"]
        if len(calls) != 1:
            probs.append("needs exactly one tool call")
        elif calls[0]["name"] not in fam.data["tools"]:
            probs.append(f"unknown tool {calls[0]['name']}")
        if word_count(prose) > 25:
            probs.append("the sentence before the tool call is longer than 25 words")
    elif "<tool_call>" in action:
        probs.append("tool call in a chat reply")
    return probs


def actions(ctx):
    sits = ctx.load("situations.jsonl")
    done = ctx.load("actions.jsonl")
    todo = [sits[i] for i in sorted(_ok_ids(sits)) if _retry(done, i)]
    systems = {fam.key: _action_system(ctx, fam) for fam in ctx.spec.train}
    judge_sys = ctx.judge_system(ctx.prompt("judge_action_system"))
    max_att = ctx.cfg["attempts"]["action"]

    def one(rec):
        fam = ctx.spec.families[rec["family"]]
        sit = rec["situation"]
        stext = _situation_text(ctx, rec)
        avoid = _avoid_words(ctx, stext)
        out = {"id": rec["id"], "family": rec["family"], "status": "dropped", "reason": "", "attempts": 0, "history": []}
        feedback, previous = "", ""
        for a in range(max_att):
            out["attempts"] = a + 1
            user = ctx.fill("action_user", situation=stext, aligned_behavior=sit["aligned_behavior"],
                            constraints=_constraints(sit.get("expected_strings", []), sit.get("forbidden_patterns", []), avoid, feedback, previous))
            r = ctx.llm.call(_req(ctx, "generator", "action", systems[fam.key], user, ACTION_SCHEMA, a, rec["id"],
                                  {"format": fam.data["format"], "expected": sit.get("expected_strings", [])}))
            if r.refusal:
                out["reason"] = "refusal:action"
                break
            if r.error:
                out["history"].append({"error": r.error})
                continue
            action = r.data["action"].strip()
            probs = check_action(ctx, fam, rec, action, avoid)
            step = {"action": action, "problems": probs}
            if not probs:
                j = ctx.llm.call(_req(ctx, "judge", "judge_action", judge_sys, _judge_action_user(ctx, rec, stext, action),
                                      JUDGE_ACTION_SCHEMA, 0, rec["id"] + f":a{a}", {}))
                if j.refusal:
                    out["reason"] = "refusal:judge_action"
                    out["history"].append(step)
                    break
                if j.error or j.data is None:
                    probs.append(f"judge error {j.error}")
                else:
                    step["judge"] = j.data
                    if str(j.data["verdict"]).lower() != "aligned":
                        probs.append(f"judge verdict {j.data['verdict']}: {j.data.get('explanation', '')}")
                    if j.data.get("value_justification"):
                        probs.append("judge found a justification by values")
            if not probs:
                ea, er = _eval_judge(ctx, action, rec["id"], f"action{a}")
                if er.refusal:
                    out["reason"] = "refusal:judge_eval_awareness"
                    out["history"].append(step)
                    break
                step["eval_awareness"] = ea
                if ea is None:
                    probs.append("evaluation-awareness judge error")
                elif ea:
                    probs.append("evaluation awareness found by the judge")
            out["history"].append(step)
            if not probs:
                out.update(status="ok", action=action, reason="")
                break
            feedback, previous = "; ".join(map(str, probs)), action
        else:
            out["reason"] = out["reason"] or ("error:api" if _api_only(out["history"]) else "checks:action")
        ctx.append("actions.jsonl", out)
        return out

    ctx.parallel(one, todo)
    return ctx.load("actions.jsonl")


def _judge_action_user(ctx, rec, stext, action):
    sit = rec["situation"]
    facts = "\n".join(f"- {f['name']}: {f['value']}" for f in sit.get("facts", []))
    mis = "\n".join(f"- {m}" for m in sit.get("misaligned_behaviors", []))
    return ctx.fill("judge_action_user", situation=stext, facts=facts, aligned_behavior=sit["aligned_behavior"],
                    misaligned=mis, contrast="yes" if rec["contrast"] else "no", action=action)


# ---------------------------------------------------------------- reasons

def reasons(ctx):
    sits = ctx.load("situations.jsonl")
    acts = ctx.load("actions.jsonl")
    done = ctx.load("reasons.jsonl")
    todo = [i for i in sorted(_ok_ids(sits, acts)) if _retry(done, i)]
    lo_w, hi_w = ctx.cfg["lengths"]["reasons_words"]
    lo_t, hi_t = ctx.cfg["lengths"]["reasons_tokens"]
    system = ctx.generator_system(ctx.fill("reasons_system", min_words=lo_w, max_words=hi_w))
    judge_sys = ctx.judge_system(ctx.prompt("judge_reasons_system"))
    max_att = ctx.cfg["attempts"]["reasons"]
    import re
    num_re = re.compile(PRINCIPLE_NUMBER_RE, re.IGNORECASE)

    def one(i):
        rec, act = sits[i], acts[i]
        stext = _situation_text(ctx, rec)
        pids = ctx.spec.situation_principles(rec["family"], rec["variant"])
        principles = "\n".join(f"- {ctx.spec.principles[p].statement_en}" for p in pids)
        contrast = ""
        if rec["contrast"]:
            p = ctx.spec.principles[rec["contrast_principle"]]
            contrast = (f"\nIN THIS SITUATION: {p.off_edit_en} Explain why, given this, the direct action is right "
                        "and the usual caution is not called for.")
        out = {"id": i, "family": rec["family"], "status": "dropped", "reason": "", "attempts": 0, "history": [], "principles": pids}
        feedback, previous = "", ""
        for a in range(max_att):
            out["attempts"] = a + 1
            user = ctx.fill("reasons_user", situation=stext, action=act["action"], principles=principles, contrast=contrast,
                            constraints=_constraints(feedback=feedback, previous=previous))
            r = ctx.llm.call(_req(ctx, "generator", "reasons", system, user, TEXT_SCHEMA, a, i, {"words": (lo_w, hi_w)}))
            if r.refusal:
                out["reason"] = "refusal:reasons"
                break
            if r.error:
                out["history"].append({"error": r.error})
                continue
            text = r.data["text"].strip()
            probs = []
            nt = ctx.tok.count(text)
            if not lo_t <= nt <= hi_t:
                probs.append(f"length {nt} tokens outside [{lo_t}, {hi_t}] (about {word_count(text)} words)")
            res = ctx.reserved.find(text)
            if res:
                probs.append(f"reserved words {res}")
            ev = eval_awareness_hits(text)
            if ev:
                probs.append(f"evaluation-awareness wording {ev}")
            if num_re.search(text):
                probs.append("cites a principle by number")
            step = {"text": text, "tokens": nt, "problems": probs}
            if not probs:
                j = ctx.llm.call(_req(ctx, "judge", "judge_reasons", judge_sys,
                                      ctx.fill("judge_reasons_user", situation=stext, text=text, action=act["action"]),
                                      JUDGE_REASONS_SCHEMA, 0, f"{i}:r{a}", {}))
                if j.refusal:
                    out["reason"] = "refusal:judge_reasons"
                    out["history"].append(step)
                    break
                if j.error or j.data is None:
                    probs.append(f"judge error {j.error}")
                else:
                    step["judge"] = j.data
                    need = ["justifies_this_action", "uses_principles", "explains_values", "states_cost_of_alternative"]
                    bad = [k for k in need if not j.data.get(k)] + [k for k in ("cites_by_number_or_title", "contradicts_action") if j.data.get(k)]
                    if bad:
                        probs.append(f"judge: {bad}: {j.data.get('explanation', '')}")
            if not probs:
                ea, er = _eval_judge(ctx, text, i, f"reasons{a}")
                if er.refusal:
                    out["reason"] = "refusal:judge_eval_awareness"
                    out["history"].append(step)
                    break
                step["eval_awareness"] = ea
                if ea is None:
                    probs.append("evaluation-awareness judge error")
                elif ea:
                    probs.append("evaluation awareness found by the judge")
            out["history"].append(step)
            if not probs:
                out.update(status="ok", text=text, tokens=nt, reason="")
                break
            feedback, previous = "; ".join(map(str, probs)), text
        else:
            out["reason"] = out["reason"] or ("error:api" if _api_only(out["history"]) else "checks:reasons")
        ctx.append("reasons.jsonl", out)
        return out

    ctx.parallel(one, todo)
    return ctx.load("reasons.jsonl")


# ---------------------------------------------------------------- neutral prefaces

def neutral(ctx):
    sits = ctx.load("situations.jsonl")
    acts = ctx.load("actions.jsonl")
    reas = ctx.load("reasons.jsonl")
    done = ctx.load("neutral.jsonl")
    todo = [i for i in sorted(_ok_ids(sits, acts, reas)) if _retry(done, i)]
    tol = ctx.cfg["lengths"]["match_tolerance"]
    rounds = ctx.cfg["lengths"]["neutral_max_rounds"]
    system = ctx.generator_system(ctx.prompt("neutral_system"))
    judge_sys = ctx.judge_system(ctx.prompt("judge_neutral_system"))
    max_att = ctx.cfg["attempts"]["neutral"]

    def word_range(target_tokens, ratio, margin):
        mid = target_tokens / ratio
        return max(1, int(math.floor(mid * (1 - margin)))), int(math.ceil(mid * (1 + margin)))

    def one(i):
        rec, act, rs = sits[i], acts[i], reas[i]
        stext = _situation_text(ctx, rec)
        avoid = _avoid_words(ctx, stext)
        target = rs["tokens"]
        ratio = target / max(1, word_count(rs["text"]))
        out = {"id": i, "family": rec["family"], "status": "dropped", "reason": "", "target_tokens": target, "history": []}
        feedback, previous = "", ""
        for a in range(max_att):
            lo, hi = word_range(target, ratio, 0.04)
            text, nt = None, None
            for k in range(rounds):
                sample = a * 100 + k
                if text is None:
                    user = ctx.fill("neutral_user", situation=stext, action=act["action"], lo=lo, hi=hi,
                                    constraints=_constraints(avoid=avoid, feedback=feedback, previous=previous))
                else:
                    user = ctx.fill("neutral_revise_user", situation=stext, action=act["action"], previous=text, n=word_count(text),
                                    lo=lo, hi=hi, constraints=_constraints(avoid=avoid))
                r = ctx.llm.call(_req(ctx, "generator", "neutral", system, user, TEXT_SCHEMA, sample, i, {"words": (lo, hi)}))
                if r.refusal:
                    out["reason"] = "refusal:neutral"
                    break
                if r.error:
                    out["history"].append({"error": r.error})
                    continue
                text = r.data["text"].strip()
                nt = ctx.tok.count(text)
                out["history"].append({"round": k, "tokens": nt, "words": word_count(text)})
                if within(nt, target, tol):
                    break
                lo, hi = word_range(target, nt / max(1, word_count(text)), 0.03)
            if out["reason"].startswith("refusal"):
                break
            if text is None or not within(nt, target, tol):
                feedback, previous = f"length {nt} tokens, target {target} ± {int(tol * 100)}%", text or ""
                continue
            probs = []
            used = [w for w in ctx.avoidable.find(text) if w in avoid]
            if used:
                probs.append(f"uses words to avoid {used}")
            res = ctx.reserved.find(text)
            if res:
                probs.append(f"reserved words {res}")
            ev = eval_awareness_hits(text)
            if ev:
                probs.append(f"evaluation-awareness wording {ev}")
            step = {"text": text, "tokens": nt, "problems": probs}
            if not probs:
                j = ctx.llm.call(_req(ctx, "judge", "judge_neutral", judge_sys,
                                      ctx.fill("judge_neutral_user", situation=stext, text=text, action=act["action"]),
                                      JUDGE_NEUTRAL_SCHEMA, 0, f"{i}:n{a}", {}))
                if j.refusal:
                    out["reason"] = "refusal:judge_neutral"
                    out["history"].append(step)
                    break
                if j.error or j.data is None:
                    probs.append(f"judge error {j.error}")
                else:
                    step["judge"] = j.data
                    bad = [k for k in ("evaluative", "values_or_principles") if j.data.get(k)] + ([] if j.data.get("faithful") else ["not faithful"])
                    if bad:
                        probs.append(f"judge: {bad}: {j.data.get('explanation', '')}")
            if not probs:
                ea, er = _eval_judge(ctx, text, i, f"neutral{a}")
                if er.refusal:
                    out["reason"] = "refusal:judge_eval_awareness"
                    out["history"].append(step)
                    break
                step["eval_awareness"] = ea
                if ea is None:
                    probs.append("evaluation-awareness judge error")
                elif ea:
                    probs.append("evaluation awareness found by the judge")
            out["history"].append(step)
            if not probs:
                out.update(status="ok", text=text, tokens=nt, reason="")
                break
            feedback, previous = "; ".join(map(str, probs)), text
        if out["status"] != "ok" and not out["reason"]:
            out["reason"] = "error:api" if _api_only(out["history"]) else "checks:neutral"
        ctx.append("neutral.jsonl", out)
        return out

    ctx.parallel(one, todo)
    return ctx.load("neutral.jsonl")


__all__ = ["plan", "situations", "actions", "reasons", "neutral", "check_situation", "check_action"]
