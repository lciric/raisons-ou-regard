"""Matching of the other-situation reasoning, assembly of the arms, audit sample, report and manifest.

Programme v1.5 adds two arms to the four of the pipeline v0.1 (part 3):
- generic_principles: a fixed text of principles (spec/generic_principles.json), the same for every item, in the slot;
- reflection: the slot empty and the action, as in actions_only; then, in a branch, a fixed question of reflection and
  the item's reasons as the answer. The loss covers both assistant turns ("loss": "assistant_all"), so that the arm
  learns the identical action and the reasons, which it never writes before acting.
"""
import csv
import hashlib
import json
import os
import random
from collections import Counter, defaultdict, deque

from .render import chat_messages, render_situation, tools_block, with_preface
from .textutil import NgramIndex, eval_awareness_hits
from .tokens import within

PREFACE_ARMS = ["actions_only", "neutral_text", "other_reasoning", "generic_principles", "reasons"]
ARMS = PREFACE_ARMS + ["reflection"]
# The subset of another family (programme v1.5, part 3): the same items, with the reasons, or the neutral texts, of the
# main generator and of the generator of another family. They are comparison arms, trained on the subset alone.
SUBSET_ARMS = ["subset_reasons_main", "subset_reasons_other", "subset_neutral_main", "subset_neutral_other"]
GENERIC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "spec", "generic_principles.json")


def _jsonl(path):
    with open(path, encoding="utf8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def _json(path):
    with open(path, encoding="utf8") as fh:
        return json.load(fh)


def _sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ---------------------------------------------------------------- matching

def hopcroft_karp(adj, left):
    """Maximum bipartite matching. adj[u] lists the right vertices of left vertex u. Returns {u: v}."""
    import sys
    sys.setrecursionlimit(max(sys.getrecursionlimit(), 4 * len(left) + 1000))
    INF = float("inf")
    match_l, match_r, dist = {u: None for u in left}, {}, {}

    def bfs():
        q = deque()
        for u in left:
            if match_l[u] is None:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = INF
        while q:
            u = q.popleft()
            if dist[u] < found:
                for v in adj[u]:
                    w = match_r.get(v)
                    if w is None:
                        if found == INF:
                            found = dist[u] + 1
                    elif dist[w] == INF:
                        dist[w] = dist[u] + 1
                        q.append(w)
        return found != INF

    def dfs(u):
        for v in adj[u]:
            w = match_r.get(v)
            if w is None or (dist[w] == dist[u] + 1 and dfs(w)):
                match_l[u] = v
                match_r[v] = u
                return True
        dist[u] = INF
        return False

    while bfs():
        for u in left:
            if match_l[u] is None:
                dfs(u)
    return {u: v for u, v in match_l.items() if v is not None}


def _stratum(c):
    return (bool(c.get("contrast")), c.get("variant"))


def select_stratified(candidates, target):
    """Per family, picks target items keeping the planned shares of contrast and variants (strata), by index order.

    candidates: {id: {"family", "index", "contrast", "variant", "planned": {stratum: share}}}.
    Returns (selected ids, {family: [surplus ids in index order]}).
    """
    by_fam = defaultdict(list)
    for i, c in sorted(candidates.items(), key=lambda kv: kv[1]["index"]):
        by_fam[c["family"]].append(i)
    selected, surplus = set(), {}
    for fam, ids in by_fam.items():
        planned = candidates[ids[0]].get("planned") or {}
        quotas = {s: int(round(share * target)) for s, share in planned.items()}
        chosen = []
        for s, q in quotas.items():
            chosen += [i for i in ids if _stratum(candidates[i]) == s][:q]
        rest = [i for i in ids if i not in set(chosen)]
        chosen += rest[:max(0, target - len(chosen))]
        chosen = chosen[:target]
        selected |= set(chosen)
        surplus[fam] = [i for i in ids if i not in set(chosen)]
    return selected, surplus


def match_other_reasoning(ctx, candidates):
    """Picks, for each situation, the reasons written for a situation of a family with no principle in common, at
    matched length; each reason text is used once, so the arm is a permutation of the reasons arm when the matching
    is perfect. Unmatched situations are replaced from the surplus of their family (same stratum first), then dropped.

    candidates: {id: {"family", "index", "tokens", "contrast", "variant", "planned"}} for every situation with
    valid reasons and neutral preface. Returns (selected ids, {target: donor}, log).
    """
    target = ctx.cfg["sizes"]["target_per_family"]
    tol = ctx.cfg["lengths"]["match_tolerance"]
    rng = random.Random(f"{ctx.cfg['seed']}:match")
    selected, queue = select_stratified(candidates, target)
    donors_of = {f.key: set(ctx.spec.donor_families(f.key)) for f in ctx.spec.train}
    log = []
    m = {}
    for rnd in range(50):
        sel = sorted(selected)
        adj = {}
        for t in sel:
            ft, nt = candidates[t]["family"], candidates[t]["tokens"]
            opts = [d for d in sel if d != t and candidates[d]["family"] in donors_of[ft] and within(candidates[d]["tokens"], nt, tol)]
            rng.shuffle(opts)
            adj[t] = opts
        m = hopcroft_karp(adj, sel)
        unmatched = [t for t in sel if t not in m]
        log.append({"round": rnd, "selected": len(sel), "matched": len(m), "unmatched": len(unmatched)})
        if not unmatched:
            return selected, m, log
        replaced = False
        for t in unmatched:
            fam = candidates[t]["family"]
            pool = queue.get(fam, [])
            if pool:
                same = [i for i in pool if _stratum(candidates[i]) == _stratum(candidates[t])]
                pick = same[0] if same else pool[0]
                pool.remove(pick)
                selected.discard(t)
                selected.add(pick)
                replaced = True
        if not replaced:
            for t in unmatched:
                selected.discard(t)
    return selected, {t: d for t, d in m.items() if t in selected and d in selected}, log


# ---------------------------------------------------------------- assembly

def assemble(ctx, allow_unchecked=False):
    """Builds the arms. Refuses to finish when a gate is not met, unless allow_unchecked (dry runs)."""
    sits, acts = ctx.load("situations.jsonl"), ctx.load("actions.jsonl")
    reas, neut = ctx.load("reasons.jsonl"), ctx.load("neutral.jsonl")
    ok = [i for i in sits if all(m.get(i, {}).get("status") == "ok" for m in (sits, acts, reas, neut))]
    plan = ctx.load("plan.jsonl")
    planned = defaultdict(Counter)
    for r in plan.values():
        planned[r["family"]][_stratum(r)] += 1
    shares = {f: {s: k / sum(c.values()) for s, k in c.items()} for f, c in planned.items()}
    cands = {i: {"family": sits[i]["family"], "index": sits[i]["index"], "tokens": reas[i]["tokens"], "contrast": sits[i]["contrast"],
                 "variant": sits[i]["variant"], "planned": shares[sits[i]["family"]]} for i in ok}
    selected, donor, mlog = match_other_reasoning(ctx, cands)
    final = sorted(i for i in selected if i in donor)
    gates = {}
    gates["tokenizer"] = "approximate" if ctx.tok.approximate else "exact"

    o, c = ctx.cfg["preface"]["open"], ctx.cfg["preface"]["close"]
    tol = ctx.cfg["lengths"]["match_tolerance"]
    generic = _json(GENERIC)
    t_g = ctx.tok.count(generic["text"])
    arms = {a: [] for a in ARMS}
    items = []
    problems = []
    for i in final:
        rec = sits[i]
        fam = ctx.spec.families[rec["family"]]
        tb = tools_block(ctx.spec, fam)
        action = acts[i]["action"]
        # recount with the current tokenizer: the gate on lengths is checked on what is written
        t_r = ctx.tok.count(reas[i]["text"])
        t_n = ctx.tok.count(neut[i]["text"])
        t_o = ctx.tok.count(reas[donor[i]]["text"])
        if not (within(t_n, t_r, tol) and within(t_o, t_r, tol)):
            problems.append(f"{i}: lengths reasons={t_r} neutral={t_n} other={t_o} outside ±{tol:.0%}")
        prefaces = {"actions_only": "", "neutral_text": neut[i]["text"], "other_reasoning": reas[donor[i]]["text"],
                    "generic_principles": generic["text"], "reasons": reas[i]["text"]}
        targets = {}
        for a in PREFACE_ARMS:
            target = with_preface(o, c, prefaces[a], action)
            assert target.endswith("\n" + action) and target.split(c + "\n", 1)[1] == action
            targets[a] = target
            arms[a].append({"id": i, "family": rec["family"], "arm": a, "messages": chat_messages(rec["situation"], tb, target)})
        branch = chat_messages(rec["situation"], tb, targets["actions_only"]) + [
            {"role": "user", "content": generic["reflection_question"]}, {"role": "assistant", "content": reas[i]["text"]}]
        arms["reflection"].append({"id": i, "family": rec["family"], "arm": "reflection", "loss": "assistant_all", "messages": branch})
        items.append({"id": i, "family": rec["family"], "variant": rec["variant"], "contrast": rec["contrast"],
                      "donor": donor[i], "donor_family": sits[donor[i]]["family"], "action_sha256": hashlib.sha256(action.encode()).hexdigest(),
                      "tokens": {"reasons": t_r, "neutral_text": t_n, "other_reasoning": t_o, "generic_principles": t_g}})
    gates["lengths"] = "ok" if not problems else f"{len(problems)} items outside tolerance"
    # the fixed generic text matches the mean length of the reasons, within a looser tolerance: one text serves every item
    mean_r = sum(it["tokens"]["reasons"] for it in items) / max(1, len(items))
    gtol = ctx.cfg["lengths"].get("generic_tolerance", 0.25)
    gates["generic_length"] = "ok" if items and within(t_g, mean_r, gtol) else \
        f"generic text {t_g} tokens against a mean of {mean_r:.0f} for the reasons (±{gtol:.0%})"

    # every text of the training data, for the lexical gates
    texts = {}
    for i in final:
        rec = sits[i]
        texts[i] = "\n".join([render_situation(rec["situation"], tools_block(ctx.spec, ctx.spec.families[rec["family"]])),
                              acts[i]["action"], reas[i]["text"], neut[i]["text"]])
    texts["generic_principles"] = generic["text"] + "\n" + generic["reflection_question"]

    # the subset of another family: its items among the final ones, when both of its texts passed
    subset, sub_arms = None, {a: [] for a in SUBSET_ARMS}
    if os.path.exists(ctx.path("reasons_other.jsonl")):
        reas_o, neut_o = ctx.load("reasons_other.jsonl"), ctx.load("neutral_other.jsonl")
        drawn = set(_json(ctx.path("other_family_subset.json"))["ids"]) if os.path.exists(ctx.path("other_family_subset.json")) else set()
        sub = [i for i in final if reas_o.get(i, {}).get("status") == "ok" and neut_o.get(i, {}).get("status") == "ok"]
        sub_problems = []
        for i in sub:
            rec = sits[i]
            tb = tools_block(ctx.spec, ctx.spec.families[rec["family"]])
            action = acts[i]["action"]
            t_ro, t_no = ctx.tok.count(reas_o[i]["text"]), ctx.tok.count(neut_o[i]["text"])
            if not within(t_no, t_ro, tol):
                sub_problems.append(f"{i}: lengths reasons={t_ro} neutral={t_no} outside ±{tol:.0%} (other family)")
            for a, text in (("subset_reasons_main", reas[i]["text"]), ("subset_reasons_other", reas_o[i]["text"]),
                            ("subset_neutral_main", neut[i]["text"]), ("subset_neutral_other", neut_o[i]["text"])):
                sub_arms[a].append({"id": i, "family": rec["family"], "arm": a,
                                    "messages": chat_messages(rec["situation"], tb, with_preface(o, c, text, action))})
            texts[f"{i}:other_family"] = reas_o[i]["text"] + "\n" + neut_o[i]["text"]
        subset = {"drawn": len(drawn), "final": len(sub), "length_problems": sub_problems,
                  "dropped": sorted(drawn - set(sub))}
    reserved_hits = {i: ctx.reserved.find(t) for i, t in texts.items()}
    reserved_hits = {i: h for i, h in reserved_hits.items() if h}
    gates["reserved_lexicon"] = "ok" if not reserved_hits else f"{len(reserved_hits)} items"
    eval_hits = {i: eval_awareness_hits(t) for i, t in texts.items()}
    eval_hits = {i: h for i, h in eval_hits.items() if h}
    gates["evaluation_awareness_patterns"] = "ok" if not eval_hits else f"{len(eval_hits)} items"

    ng = ctx.cfg["ngram"]
    ngram_hits = {}
    if ng.get("heldout_corpus") and os.path.exists(_res(ng["heldout_corpus"])):
        if ng["unit"] == "tokens" and ctx.tok.approximate and not allow_unchecked:
            raise RuntimeError("the n-gram gate on tokens needs the real tokenizer")
        wl = []
        if ng.get("whitelist") and os.path.exists(_res(ng["whitelist"])):
            with open(_res(ng["whitelist"]), encoding="utf8") as fh:
                wl = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
        idx = NgramIndex(ng["n"], ng["unit"], tokenizer=ctx.tok, whitelist=wl)
        for r in _jsonl(_res(ng["heldout_corpus"])):
            idx.add(r["id"], r["text"])
        for i, t in texts.items():
            ov = idx.overlaps(t)
            if ov:
                ngram_hits[i] = ov
        gates["ngrams"] = "ok" if not ngram_hits else f"{len(ngram_hits)} items"
    else:
        gates["ngrams"] = "not run: the held-out scenarios do not exist yet"

    cue_hits = {}
    cue_files = [f for f in ctx.cfg.get("cues", {}).get("files", []) if os.path.exists(_res(f))]
    if cue_files:
        cues = []
        for f in cue_files:
            cues += [r["text"] for r in _jsonl(_res(f))]
        for i, t in texts.items():
            low = t.lower()
            h = [q for q in cues if q.lower() in low]
            if h:
                cue_hits[i] = h[:3]
        gates["cues"] = "ok" if not cue_hits else f"{len(cue_hits)} items"
    else:
        gates["cues"] = "not run: the cue sets do not exist yet"

    # Mini-spec v0.2, §6 and §8 point 8: the affective balance of cue pairs and of the texts between arms is read by the
    # starting model on GPU (projections on the directions of the reading base), not by this text pipeline.
    gates["affective_matching"] = "not run: GPU stage (projections of the arm texts and cue pairs, |d| < %s)" % ctx.cfg.get("affect", {}).get("max_abs_d", 0.2)
    blocking = [k for k, v in gates.items() if v != "ok" and not (k == "tokenizer" and v == "exact")]
    for a in ARMS:
        ctx.write(f"arms/{a}.jsonl", arms[a])
    if subset is not None:
        for a in SUBSET_ARMS:
            ctx.write(f"arms/{a}.jsonl", sub_arms[a])
    ctx.write("final_items.jsonl", items)
    with open(ctx.path("gates.json"), "w", encoding="utf8") as fh:
        json.dump({"gates": gates, "blocking": blocking, "length_problems": problems, "reserved_hits": reserved_hits,
                   "evaluation_awareness_hits": eval_hits, "ngram_hits": ngram_hits, "cue_hits": cue_hits, "matching": mlog,
                   "other_family": subset}, fh, ensure_ascii=False, indent=1)
    if blocking and not allow_unchecked:
        raise RuntimeError(f"assembly written but not final: gates not met {blocking} (see gates.json)")
    return {"final": len(final), "gates": gates, "blocking": blocking,
            "other_family": None if subset is None else subset["final"]}


def _res(p):
    from .context import resolve
    return resolve(p)


# ---------------------------------------------------------------- audit

def audit(ctx):
    """Stratified sample for the human audit: about n items, the same number per family and arm."""
    n = ctx.cfg["audit"]["n"]
    sits, acts = ctx.load("situations.jsonl"), ctx.load("actions.jsonl")
    items = _jsonl(ctx.path("final_items.jsonl"))
    arms = {a: {r["id"]: r for r in _jsonl(ctx.path(f"arms/{a}.jsonl"))} for a in ARMS}
    fams = sorted({it["family"] for it in items})
    if not fams:
        return {"rows": 0, "per_cell": 0, "path": None, "note": "no final item: nothing to audit"}
    per = max(1, n // (len(fams) * len(ARMS)))
    rng = random.Random(f"{ctx.cfg['seed']}:audit")
    rows = []
    for f in fams:
        ids = sorted(it["id"] for it in items if it["family"] == f)
        for a in ARMS:
            for i in rng.sample(ids, min(per, len(ids))):
                ex = arms[a][i]
                fam = ctx.spec.families[f]
                rows.append({"item": i, "family": f, "arm": a,
                             "situation": render_situation(sits[i]["situation"], tools_block(ctx.spec, fam)),
                             "assistant_turn": ex["messages"][-1]["content"],
                             "aligned_behavior": sits[i]["situation"]["aligned_behavior"],
                             "judge_verdict": acts[i]["history"][-1].get("judge", {}).get("verdict", ""),
                             "human_action_aligned": "", "human_preface_fits_arm": "", "human_eval_awareness": "", "notes": ""})
    p = ctx.path("audit/audit_sheet.csv")
    with open(p, "w", encoding="utf8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return {"rows": len(rows), "per_cell": per, "path": p}


def audit_agreement(ctx, sheet_path):
    """Agreement between the human labels (yes/no) and the judge verdicts, once the sheet is filled."""
    with open(sheet_path, encoding="utf8") as fh:
        rows = list(csv.DictReader(fh))
    pairs = [(r["human_action_aligned"].strip().lower() in ("yes", "oui", "1", "true"), r["judge_verdict"].strip().lower() == "aligned")
             for r in rows if r["human_action_aligned"].strip()]
    if not pairs:
        return {"n": 0}
    n = len(pairs)
    agree = sum(a == b for a, b in pairs) / n
    ph = sum(a for a, _ in pairs) / n
    pj = sum(b for _, b in pairs) / n
    pe = ph * pj + (1 - ph) * (1 - pj)
    kappa = (agree - pe) / (1 - pe) if pe < 1 else 1.0
    return {"n": n, "agreement": round(agree, 3), "kappa": round(kappa, 3)}


# ---------------------------------------------------------------- report and manifest

def report(ctx):
    sits, acts = ctx.load("situations.jsonl"), ctx.load("actions.jsonl")
    reas, neut = ctx.load("reasons.jsonl"), ctx.load("neutral.jsonl")
    final = _jsonl(ctx.path("final_items.jsonl")) if os.path.exists(ctx.path("final_items.jsonl")) else []
    gates = _json(ctx.path("gates.json")) if os.path.exists(ctx.path("gates.json")) else {}
    calls = _jsonl(ctx.path("logs/calls.jsonl")) if os.path.exists(ctx.path("logs/calls.jsonl")) else []

    fams = [f.key for f in ctx.spec.train]
    L = [f"# Rapport du pipeline de données — {ctx.cfg['run_name']}{' (simulation hors ligne)' if ctx.mock else ''}", ""]
    L += ["## Effectifs par étape", "", "| Famille | Prévues | Situations | Actions | Raisons | Textes neutres | Retenues |", "|---|---|---|---|---|---|---|"]
    plan = ctx.load("plan.jsonl")
    for f in fams:
        cnt = lambda m: sum(1 for r in m.values() if r.get("family") == f and r.get("status") == "ok")
        L.append(f"| {f} | {sum(1 for r in plan.values() if r['family'] == f)} | {cnt(sits)} | {cnt(acts)} | {cnt(reas)} | {cnt(neut)} | "
                 f"{sum(1 for r in final if r['family'] == f)} |")
    L += ["", "## Pertes, par raison", ""]
    reasons_count = Counter()
    for name, m in (("situations", sits), ("actions", acts), ("raisons", reas), ("textes neutres", neut)):
        for r in m.values():
            if r.get("status") != "ok":
                reasons_count[(name, r.get("reason", ""))] += 1
    for (name, why), k in sorted(reasons_count.items()):
        L.append(f"- {name} : {why or 'inconnue'} : {k}")
    refusals = Counter(c["stage"] for c in calls if c.get("refusal") and not c.get("cached"))
    L += ["", "## Refus (jamais rejoués ni reformulés)", ""] + ([f"- {s} : {k}" for s, k in sorted(refusals.items())] or ["- aucun"])

    L += ["", "## Parts dans les situations retenues", ""]
    for f in fams:
        fr = [r for r in final if r["family"] == f]
        if fr:
            L.append(f"- {f} : contraste {sum(r['contrast'] for r in fr) / len(fr):.0%} ; variante {sum(1 for r in fr if r['variant']) / len(fr):.0%}")
    L += ["", "## Ressemblance des situations à une évaluation (juge de réalisme, p moyen)", ""]
    for f in fams:
        ps = [r["realism"]["p_evaluation"] for r in sits.values() if r.get("family") == f and r.get("status") == "ok" and isinstance(r.get("realism", {}).get("p_evaluation"), (int, float))]
        if ps:
            L.append(f"- {f} : {sum(ps) / len(ps):.2f} sur {len(ps)} situations")
    L += ["", "## Conscience d'évaluation dans les textes générés", ""]
    for name, m in (("actions", acts), ("raisons", reas), ("textes neutres", neut)):
        steps = [s for r in m.values() for s in r.get("history", []) if "eval_awareness" in s]
        flagged = sum(1 for s in steps if s["eval_awareness"])
        pat = sum(1 for r in m.values() for s in r.get("history", []) for p in s.get("problems", []) if "evaluation-awareness wording" in str(p))
        L.append(f"- {name} : {flagged} signalés par le juge sur {len(steps)} textes jugés ; {pat} écartés par les motifs avant le juge")
    L += ["", "## Appariement du raisonnement d'une autre situation", ""]
    if final:
        pairs = Counter((r["family"], r["donor_family"]) for r in final)
        for (a, b), k in sorted(pairs.items()):
            L.append(f"- {a} ← {b} : {k}")
        perm = len({r['donor'] for r in final}) == len(final) and {r['donor'] for r in final} == {r['id'] for r in final}
        L.append(f"- permutation exacte des raisons : {'oui' if perm else 'non'}")
    L += ["", "## Portes", ""] + [f"- {k} : {v}" for k, v in gates.get("gates", {}).items()]
    L += ["", "## Appels et coût", ""]
    live = [c for c in calls if not c.get("cached") and not c.get("error")]
    by_model = defaultdict(lambda: Counter())
    for c in live:
        for k, v in (c.get("usage") or {}).items():
            by_model[c["model"]][k] += v
        by_model[c["model"]]["calls"] += 1
    total = 0.0
    for model, u in by_model.items():
        p = (ctx.cfg.get("prices_usd_per_mtok") or {}).get(model)
        cost = None
        if p:
            cost = (u["input"] * p["input"] + u["output"] * p["output"] + u["cache_write"] * p["cache_write_5m"] + u["cache_read"] * p["cache_read"]) / 1e6
            total += cost
        L.append(f"- {model} : {u['calls']} appels ; entrée {u['input']:,} ; sortie {u['output']:,} ; cache écrit {u['cache_write']:,} ; cache lu {u['cache_read']:,}"
                 + (f" ; {cost:,.2f} $" if cost is not None else ""))
    L.append(f"- total estimé : {total:,.2f} $ (prix standard, hors traitement par lots)")
    with open(ctx.path("RAPPORT.md"), "w", encoding="utf8") as fh:
        fh.write("\n".join(L) + "\n")
    return ctx.path("RAPPORT.md")


def manifest(ctx):
    files = {}
    for root, _, names in os.walk(ctx.out):
        for n in sorted(names):
            if n.endswith(".sqlite") or n.endswith(".tmp"):
                continue
            p = os.path.join(root, n)
            rel = os.path.relpath(p, ctx.out)
            if rel == "manifest.json":
                continue
            files[rel] = _sha(p)
    m = {"run": ctx.cfg["run_name"], "mock": ctx.mock, "code_version": ctx.code_version(),
         "config": ctx.cfg, "config_sha256": _sha(ctx.config_path),
         "spec_sha256": {n: _sha(_res(f"spec/{n}")) for n in ("principles.json", "families.json")},
         "prompts_sha256": ctx.prompt_hashes(), "backends": {r: b.describe() for r, b in ctx.llm.backends.items()},
         "tokenizer": ctx.tok.describe(), "files_sha256": files}
    with open(ctx.path("manifest.json"), "w", encoding="utf8") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=1)
    return ctx.path("manifest.json")
