"""The four disjoint cue sets and the deployment prompt (mini-spec v0.2, §6), and the neutral contexts they frame.

- The extraction, validation and framing sets are snippets: an evaluation cue and a deployment cue, written as a
  matched pair (same place, register and length), to insert before the same neutral context.
- The fresh-probe set is made of rewrites: the same request, once with the marks of a constructed test item and once
  with the noise of real use.
- The sets are disjoint by mechanism (each set has its own) and by vocabulary: no content-word trigram of a cue is
  shared with an earlier set; a colliding pair is dropped and the surplus replaces it.
- No cue of any set may appear in the training data: the assembly gate reads the exported files (config cues.files).
- Decision 24 (October 3, 2026), after the first extraction on the starting model:
  - the validation set shares no evaluation or deployment vocabulary with the extraction set: a validation pair is
    dropped if one of its words has the stem of a word that leans to one side of the extraction set
    (rrdata.lexical.polar_vocabulary), and the generator is told these words;
  - the two rewrites of a fresh-probe pair have the same length (within a tenth) and the same register (the register is
    drawn per pair and given to both; a proxy of informality is checked);
  - the report gives the lexical baseline (a bag of words learned on the extraction set) on every other set, and the
    gates of the rules in spec/cues.json "rules" (thresholds: proposals).
- A build can reuse sets and contexts of an earlier run (config cue_build): they are kept as they are, and the new
  sets must be disjoint from them.

The affective balance of the pairs (mini-spec v0.2, §6) is read on GPU by the starting model, not here.
"""
import json
import math
import random
import re

from .lexical import auroc, lexical_auroc, polar_vocabulary, shared_words
from .schemas import obj, STR
from .textutil import STOPWORDS, jaccard, sha256_text, words

CONTEXTS_SCHEMA = obj({"contexts": {"type": "array", "items": obj({"domain": STR, "text": STR})}})
PAIRS_SCHEMA = obj({"pairs": {"type": "array", "items": obj({"eval": STR, "deploy": STR})}})
FRESH_SCHEMA = obj({"eval": STR, "deploy": STR})

EVAL_RE = re.compile(r"\b(?:test(?:s|ed|ing)?|evaluat\w*|eval|benchmark\w*|rubric\w*|grad(?:er|ers|ing|ed)|scor(?:e|es|ed|ing)|"
                     r"assess\w*|red[- ]?team\w*|wood\s+labs)\b", re.IGNORECASE)
DEPLOY_EXPLICIT_RE = re.compile(r"\b(?:deploy\w*|production|real[- ](?:users?|customers?|people|clients?))\b", re.IGNORECASE)
REAL_USERS_RE = re.compile(r"\breal[- ](?:users?|customers?|people|clients?)\b", re.IGNORECASE)
ITEM_COUNTER_RE = re.compile(r"\bitem\s*#?\s*\d+\s*(?:/|of)\s*\d+\b", re.IGNORECASE)
WOOD_RE = re.compile(r"\bwood\s+labs\b", re.IGNORECASE)


def load_cue_spec(ctx):
    from .context import resolve
    with open(resolve("spec/cues.json"), encoding="utf8") as fh:
        return json.load(fh)


def content_trigrams(text):
    """Trigrams of consecutive content words (function words removed), lower-cased."""
    w = [x.lower() for x in words(text) if x.lower() not in STOPWORDS]
    return {" ".join(w[i:i + 3]) for i in range(max(0, len(w) - 2))}


# Fresh probe (decision 24): the two rewrites have the same length within a tenth (or 3 words), and the same register.
FRESH_LENGTH_RATIO = 0.9
SLANG = {"u", "ur", "rn", "lol", "idk", "gonna", "wanna", "kinda", "sorta", "tbh", "btw", "pls", "plz", "thx", "ok", "okay",
         "yeah", "nah", "haha", "lmao", "omg", "ya", "yep", "nope", "cuz", "bc"}
NO_APOSTROPHE = {"dont", "cant", "im", "ive", "thats", "whats", "doesnt", "isnt", "wont", "didnt", "wasnt", "youre", "theyre", "id"}


def informality(text):
    """The kinds of informal marks a text carries: a proxy of its register, to compare the two sides of a pair."""
    t = text or ""
    low = [w.lower() for w in words(t)]
    kinds = set()
    first = next((c for c in t if c.isalpha()), "")
    if first and first.islower():
        kinds.add("lower-case start")
    if any(w in SLANG for w in low):
        kinds.add("slang")
    if any(w in NO_APOSTROPHE for w in low):
        kinds.add("missing apostrophe")
    if re.search(r"(?:^|\s)i(?:\s|$)", t):
        kinds.add("lower-case i")
    if re.search(r"[!?]{2,}", t):
        kinds.add("repeated punctuation")
    if "..." in t or "\u2026" in t:
        kinds.add("ellipsis")
    if "!" in t:
        kinds.add("exclamation")
    return kinds


def _ratio_ok(a, b, ratio=0.75, slack=3):
    na, nb = len(words(a)), len(words(b))
    if min(na, nb) == 0:
        return False
    return abs(na - nb) <= slack or ratio <= na / nb <= 1.0 / ratio


def check_pair(set_key, ev, de):
    """Programmatic checks of one cue pair. Returns a list of problems."""
    p = []
    if not ev.strip() or not de.strip():
        return ["empty cue"]
    if ev.strip().lower() == de.strip().lower():
        p.append("identical cues")
    if set_key == "fresh_probe":
        if not _ratio_ok(ev, de, FRESH_LENGTH_RATIO, 3):
            p.append(f"lengths {len(words(ev))} and {len(words(de))} words differ by more than a tenth")
        diff = informality(ev) ^ informality(de)
        if len(diff) >= 2:
            p.append(f"registers differ: {', '.join(sorted(diff))}")
    elif not _ratio_ok(ev, de):
        p.append(f"lengths {len(words(ev))} and {len(words(de))} words differ by more than a quarter")
    limit = 140 if set_key == "fresh_probe" else 90
    if max(len(words(ev)), len(words(de))) > limit:
        p.append(f"longer than {limit} words")
    if EVAL_RE.search(de):
        p.append(f"deployment cue mentions evaluation: {EVAL_RE.search(de).group(0)!r}")
    if REAL_USERS_RE.search(ev):
        p.append("evaluation cue mentions real users")
    if set_key in ("validation", "framing", "fresh_probe") and DEPLOY_EXPLICIT_RE.search(de):
        p.append(f"deployment cue says it is a deployment: {DEPLOY_EXPLICIT_RE.search(de).group(0)!r}")
    if set_key != "extraction" and WOOD_RE.search(ev + " " + de):
        p.append("Wood Labs belongs to the extraction set")
    if set_key in ("framing", "fresh_probe") and ITEM_COUNTER_RE.search(ev):
        p.append("item counters belong to the validation set")
    if set_key == "fresh_probe" and EVAL_RE.search(ev):
        p.append("the constructed rewrite must not say it is a test")
    if "?" in ev + de and set_key != "fresh_probe":
        p.append("a cue holds a question")
    return p


# ---------------------------------------------------------------- generation

def _call(ctx, stage, user, schema, sample, item, meta):
    from .llm import Request
    return ctx.llm.call(Request(role="generator", stage=stage, system=ctx.prompt("cues_system"), user=user, schema=schema,
                                sample=sample, item=item, meta=meta))


def _redo(done, key):
    """A batch is drawn again when its last record ended on an API error (network, credit, overload, unreadable
    answer): such a failure says nothing about the batch. A refusal or an answer, checked or not, is final (the rule of
    stages._retry for the pipeline's items)."""
    r = done.get(key)
    return r is None or (bool(r.get("error")) and not r.get("refusal"))


def contexts(ctx):
    """Neutral requests, by domain: the first ones frame the snippet sets, the next ones are rewritten by the fresh probe."""
    spec = load_cue_spec(ctx)
    domains = spec["context_domains"]
    need = sum(spec["contexts"].values())
    per = int(math.ceil(need * spec["overprovision"] / len(domains)))
    done = ctx.load("cues/context_batches.jsonl")

    def one(domain):
        bid = f"ctx-{domain}"
        if bid in done:
            return done[bid]
        r = _call(ctx, "cue_contexts", ctx.fill("cue_contexts_user", n=per, domain=domain), CONTEXTS_SCHEMA, 0, bid, {"n": per, "domain": domain})
        rec = {"id": bid, "domain": domain, "refusal": r.refusal, "error": r.error, "contexts": []}
        if r.data and not r.refusal:
            rec["contexts"] = [c["text"].strip() for c in r.data.get("contexts", []) if c.get("text", "").strip()]
        ctx.append("cues/context_batches.jsonl", rec)
        return rec

    batches = ctx.parallel(one, domains)
    # round-robin over domains, so that both uses cover every domain
    pools = [[t for t in b["contexts"] if _context_ok(t)] for b in batches]
    seen, ordered = [], []
    k = 0
    while any(pools) and len(ordered) < need:
        pool = pools[k % len(pools)]
        k += 1
        if not pool:
            continue
        t = pool.pop(0)
        sh = set(words(t.lower()))
        if any(jaccard(sh, s) > 0.6 for s in seen):
            continue
        seen.append(sh)
        ordered.append(t)
    n_snip = spec["contexts"]["snippet"]
    recs = [{"id": f"ctx-{i:04d}", "use": "snippet" if i < n_snip else "fresh", "text": t} for i, t in enumerate(ordered)]
    ctx.write("cues/contexts.jsonl", recs)
    return recs


def _context_ok(t):
    n = len(words(t))
    return 6 <= n <= 80 and not EVAL_RE.search(t) and not DEPLOY_EXPLICIT_RE.search(t)


def snippet_pairs(ctx, set_spec, extra_forbidden=()):
    """Generated pairs of one snippet set, checked; returns the candidate pairs in generation order. extra_forbidden:
    words the generator is told not to use (for the validation set, the polar words of the extraction set)."""
    spec = load_cue_spec(ctx)
    bsz = spec["batch_pairs"]
    n_batches = int(math.ceil(spec["pairs_per_set"] * spec["overprovision"] / bsz))
    rng = random.Random(f"{ctx.cfg['seed']}:cues:{set_spec['key']}")
    forbidden = {"extraction": [], "validation": ["Wood Labs"], "framing": ["Wood Labs", "benchmark", "rubric"]}.get(set_spec["key"], [])
    forbidden = forbidden + sorted(set(extra_forbidden))
    plan = []
    for b in range(n_batches):
        var = "; ".join(f"{k} = {rng.choice(v)}" for k, v in set_spec["axes"].items())
        plan.append({"id": f"{set_spec['key']}-b{b:03d}", "batch": b, "slot": set_spec["slots"][b % len(set_spec["slots"])], "variation": var})
    done = ctx.load(f"cues/{set_spec['key']}_batches.jsonl")

    def one(item):
        if not _redo(done, item["id"]):
            return done[item["id"]]
        user = ctx.fill("cue_pairs_user", n=bsz, set_key=set_spec["key"], eval_mechanism=set_spec["eval_mechanism_en"],
                        deploy_mechanism=set_spec["deploy_mechanism_en"], slot=item["slot"], variation=item["variation"],
                        forbidden=", ".join(forbidden) or "none")
        # the batch number is the sample index: two batches with the same prompt are two independent draws, not one
        # cached answer read twice
        r = _call(ctx, "cue_pairs", user, PAIRS_SCHEMA, item["batch"], item["id"], {"n": bsz, "set": set_spec["key"]})
        rec = dict(item, refusal=r.refusal, error=r.error, pairs=[])
        if r.data and not r.refusal:
            for p in r.data.get("pairs", []):
                ev, de = p.get("eval", "").strip(), p.get("deploy", "").strip()
                rec["pairs"].append({"eval": ev, "deploy": de, "problems": check_pair(set_spec["key"], ev, de)})
        ctx.append(f"cues/{set_spec['key']}_batches.jsonl", rec)
        return rec

    out = []
    for rec in ctx.parallel(one, plan):
        for p in rec["pairs"]:
            out.append(dict(p, slot=rec["slot"], batch=rec["id"]))
    return out


def fresh_pairs(ctx, set_spec, ctxs, attempts=1):
    """One pair of rewrites per fresh context. The register (and the strength of the marks) is drawn per context and
    given to both rewrites. An answer that fails the checks is drawn again, up to attempts draws in all (a refusal or
    an API error ends the draws; a context left on an API error is taken up again on the next run, where its earlier
    answers come from the cache)."""
    rng = random.Random(f"{ctx.cfg['seed']}:cues:fresh")
    todo = [c for c in ctxs if c["use"] == "fresh"]
    axes = set_spec["axes"]
    draws = {c["id"]: {k: rng.choice(v) for k, v in sorted(axes.items())} for c in todo}
    done = ctx.load("cues/fresh_probe_batches.jsonl")

    def one(c):
        bid = f"fresh-{c['id']}"
        if not _redo(done, bid):
            return done[bid]
        var = draws[c["id"]]
        rec = {"id": bid, "context": c["id"], "slot": "whole_context", "variation": var, "refusal": False, "error": None,
               "pairs": [], "draws": 0}
        for sample in range(attempts):
            user = ctx.fill("fresh_pairs_user", context=c["text"], eval_mechanism=set_spec["eval_mechanism_en"],
                            deploy_mechanism=set_spec["deploy_mechanism_en"], strength=var.get("strength", "moderate"),
                            register=var.get("register", "neutral"))
            r = _call(ctx, "fresh_pairs", user, FRESH_SCHEMA, sample, bid, {"context": c["text"]})
            rec["draws"] += 1
            rec["refusal"], rec["error"] = r.refusal, r.error
            if r.refusal or r.error or not r.data:
                break
            ev, de = r.data.get("eval", "").strip(), r.data.get("deploy", "").strip()
            problems = check_pair("fresh_probe", ev, de)
            rec["pairs"] = [{"eval": ev, "deploy": de, "problems": problems}]
            if not problems:
                break
        ctx.append("cues/fresh_probe_batches.jsonl", rec)
        return rec

    out = []
    for rec in ctx.parallel(one, todo):
        for p in rec["pairs"]:
            out.append(dict(p, slot=rec["slot"], batch=rec["id"], context=rec["context"]))
    return out


# ---------------------------------------------------------------- selection and export

def select_disjoint(candidates_by_set, order, target, fixed=None, vocabulary_rule=None, stopwords=STOPWORDS):
    """Keeps, set by set in order, the valid pairs whose cues share no content-word trigram with an earlier set and
    are not near-duplicates within their set; returns ({set: [pairs]}, {set: {reason: count}}).

    fixed: {set: [pairs]} kept as they are (reused from an earlier run); their trigrams count as taken before anything
    else. vocabulary_rule: {set: {"from": other set, "min_count", "ratio"}}: a pair of set is dropped if one of its
    words has the stem of a word that leans to one side of the other set (selected or fixed before it).
    """
    fixed = fixed or {}
    taken_grams, out, losses = set(), {}, {}
    for key, pairs in fixed.items():
        out[key], losses[key] = list(pairs), {}
        for p in pairs:
            taken_grams |= content_trigrams(p["eval"]) | content_trigrams(p["deploy"])
    for key in order:
        if key in fixed:
            continue
        banned = set()
        rule = (vocabulary_rule or {}).get(key)
        if rule:
            src = out.get(rule["from"], [])
            le, ld = polar_vocabulary([p["eval"] for p in src], [p["deploy"] for p in src], stopwords,
                                      rule.get("min_count", 2), rule.get("ratio", 3.0))
            banned = le | ld
        kept, local_grams, local_sh = [], set(), []
        loss = {}
        for p in candidates_by_set.get(key, []):
            if p["problems"]:
                loss["checks"] = loss.get("checks", 0) + 1
                continue
            if banned and (shared_words(p["eval"], banned) or shared_words(p["deploy"], banned)):
                loss[f"vocabulary of the {rule['from']} set"] = loss.get(f"vocabulary of the {rule['from']} set", 0) + 1
                continue
            grams = content_trigrams(p["eval"]) | content_trigrams(p["deploy"])
            if grams & taken_grams:
                loss["trigram shared with an earlier set"] = loss.get("trigram shared with an earlier set", 0) + 1
                continue
            sh = set(words((p["eval"] + " " + p["deploy"]).lower()))
            if any(jaccard(sh, s) > 0.7 for s in local_sh):
                loss["near duplicate"] = loss.get("near duplicate", 0) + 1
                continue
            if len(kept) >= target:
                loss["surplus"] = loss.get("surplus", 0) + 1
                continue
            kept.append(p)
            local_grams |= grams
            local_sh.append(sh)
        taken_grams |= local_grams
        out[key], losses[key] = kept, loss
    return out, losses


def _read_jsonl(path):
    with open(path, encoding="utf8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def _load_set(path):
    """The pairs of an exported cue set, in the form of the candidates."""
    pairs = {}
    for r in _read_jsonl(path):
        p = pairs.setdefault(r["pair"], {"problems": [], "slot": r["slot"], "reused_from": r["pair"]})
        p[r["polarity"]] = r["text"]
        if "context" in r:
            p["context"] = r["context"]
    return [pairs[k] for k in sorted(pairs)]


def gates(sets, rules, ctxs_by_id=None):
    """The lexical baseline on every set (a bag of words learned on the extraction set), and the gates of the rules."""
    out = {"lexical_baseline_from_extraction": {}}
    ex = sets.get("extraction", [])
    for key, pairs in sets.items():
        if key == "extraction" or not ex or not pairs:
            continue
        out["lexical_baseline_from_extraction"][key] = round(lexical_auroc(
            [p["eval"] for p in ex], [p["deploy"] for p in ex], [p["eval"] for p in pairs], [p["deploy"] for p in pairs]), 4)
    cap = rules.get("max_lexical_auroc_validation")
    if cap is not None and "validation" in out["lexical_baseline_from_extraction"]:
        a = out["lexical_baseline_from_extraction"]["validation"]
        out["validation_lexical"] = {"auroc": a, "max": cap, "passed": a <= cap}
    band = rules.get("fresh_probe_balance_band")
    fp = sets.get("fresh_probe", [])
    if band and fp:
        y = [1] * len(fp) + [0] * len(fp)
        texts = [p["eval"] for p in fp] + [p["deploy"] for p in fp]
        la = auroc([len(words(t)) for t in texts], y)
        ia = auroc([len(informality(t)) for t in texts], y)
        out["fresh_probe_balance"] = {"length_auroc": round(la, 4), "informality_auroc": round(ia, 4), "band": band,
                                      "passed": band[0] <= la <= band[1] and band[0] <= ia <= band[1]}
    return out


def build(ctx):
    """Generates everything, selects disjoint sets, writes cues/<set>.jsonl, the deployment prompt and a report.

    Config cue_build (optional): reuse_from (an earlier run's cues folder, relative to donnees/), reuse_sets (the sets
    taken from it as they are), reuse_contexts (its contexts.jsonl instead of new ones).
    """
    from .context import resolve
    spec = load_cue_spec(ctx)
    rules = spec.get("rules", {})
    order = [s["key"] for s in spec["sets"]]
    cb = ctx.cfg.get("cue_build") or {}
    src = resolve(cb["reuse_from"]) if cb.get("reuse_from") else None
    fixed = {k: _load_set(f"{src}/{k}.jsonl") for k in cb.get("reuse_sets", [])} if src else {}
    if src and cb.get("reuse_contexts"):
        ctxs = _read_jsonl(f"{src}/contexts.jsonl")
        ctx.write("cues/contexts.jsonl", ctxs)
    else:
        ctxs = contexts(ctx)
    vocab_rule = {}
    if rules.get("validation_vocabulary"):
        vocab_rule["validation"] = rules["validation_vocabulary"]
    cands = {}
    for s in spec["sets"]:
        key = s["key"]
        if key in fixed:
            continue
        if s["kind"] == "rewrite":
            cands[key] = fresh_pairs(ctx, s, ctxs, attempts=rules.get("fresh_attempts", 1))
            continue
        extra = ()
        rule = vocab_rule.get(key)
        if rule:
            # the words to avoid, told to the generator: those of the source set (fixed, or its valid candidates)
            base = fixed.get(rule["from"]) or [p for p in cands.get(rule["from"], []) if not p["problems"]]
            le, ld = polar_vocabulary([p["eval"] for p in base], [p["deploy"] for p in base], STOPWORDS,
                                      rule.get("min_count", 2), rule.get("ratio", 3.0))
            extra = sorted({w for p in base for t in (p["eval"], p["deploy"]) for w in shared_words(t, le | ld)})
        cands[key] = snippet_pairs(ctx, s, extra_forbidden=extra)
    sets, losses = select_disjoint(cands, order, spec["pairs_per_set"], fixed=fixed, vocabulary_rule=vocab_rule)
    files = []
    for key in order:
        recs = []
        for i, p in enumerate(sets[key]):
            pid = p.get("reused_from") or f"{key}-{i:04d}"
            for pol in ("eval", "deploy"):
                recs.append({"id": f"{pid}-{pol}", "pair": pid, "set": key, "polarity": pol, "slot": p["slot"], "text": p[pol],
                             **({"context": p["context"]} if "context" in p else {})})
        ctx.write(f"cues/{key}.jsonl", recs)
        files.append(f"cues/{key}.jsonl")
    with open(ctx.path("cues/deployment_prompt.txt"), "w", encoding="utf8") as fh:
        fh.write(spec["deployment_prompt"] + "\n")
    report = {"pairs": {k: len(v) for k, v in sets.items()}, "target": spec["pairs_per_set"], "losses": losses,
              "contexts": {u: sum(1 for c in ctxs if c["use"] == u) for u in ("snippet", "fresh")},
              "deployment_prompt_sha256": sha256_text(spec["deployment_prompt"]), "files": files,
              "reused": {"from": cb.get("reuse_from"), "sets": sorted(fixed), "contexts": bool(src and cb.get("reuse_contexts"))},
              "gates": gates(sets, rules),
              "complete": all(len(v) >= spec["pairs_per_set"] for v in sets.values())}
    with open(ctx.path("cues/report.json"), "w", encoding="utf8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    return report
