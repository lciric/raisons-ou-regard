"""La vérification de manipulation, lue par le transfert (programme v1.6, partie 3 ; décision 33), sur les sorties du job
de la vérification (rrexp/jobs/manipulation.py, appelé par organism_inhibition) : pour chaque condition, couche par
couche, l'AUROC de sondes apprises sur un autre jeu d'indices et lues sur le jeu tenu à part (le transfert).

Les conditions portent les noms du job : « none », « inhibition <réglage> », « comparator <i> », « control <nom> »,
« constructed failure: layer <L> only ». Chaque couche porte "transfer_linear_last", "transfer_mlp_last",
"transfer_linear_mean" et "transfer_mlp_mean".

Ce qui décide (proposé : partie 12, point 18.1, et les recommandations du 7 octobre 2026) :
- **La lecture.** Au dernier jeton, l'écart au hasard couche par couche, |AUROC − 0,5|, puis sa moyenne sur les couches.
  Un transfert sous 0,5 ne vaut pas mieux que 0,5 : une sonde qui lit à l'envers lit encore.
- **Dans un entraînement** (un bras, une graine, un réglage) : sous l'inhibition, cette moyenne est plus basse que sous
  95 % d'au moins 20 tirages appariés du comparateur, pour la sonde linéaire et pour le petit perceptron. Avec moins de
  20 tirages, la vérification n'est qu'indicative.
- **Son cas connu, l'échec construit** (l'inhibition à une seule couche) : le transfert baisse à cette couche ; en aval,
  il revient plus près de la condition sans intervention que de l'inhibition ; et l'échec ne passe pas le critère.
  Sinon, la vérification ne sait pas voir un échec, et elle ne compte pas.
- **Dans un bras** : elle tient si elle tient dans chacun de ses entraînements.
- **Entre deux bras** : l'écart au hasard sous inhibition est égal, à ± la marge près (0,05, recommandé), par
  l'intervalle à 90 % des différences graine par graine (les graines sont partagées entre bras), pour les deux sondes.
  Si l'IC à 95 % exclut 0, le bras où le transfert reste plus haut échoue : c'est la ligne 12 de la règle du regard.
  L'intervalle est celui du bootstrap sur les graines et, sous huit graines, le plus large de lui et de celui de
  Student (partie 7).
"""
import math
import re

import numpy as np

from regle_du_regard import t_quantile

PROBES = ("linear", "mlp")


def kind(name):
    """La sorte d'une condition, d'après son nom dans le job."""
    if name == "none":
        return "none"
    for prefix, k in (("inhibition", "inhibition"), ("comparator", "comparator"), ("control", "control"),
                      ("constructed failure", "failure")):
        if name.startswith(prefix):
            return k
    return "other"


def failure_layer(name):
    """La couche de l'échec construit, lue dans son nom."""
    m = re.search(r"layer (\d+)", name)
    return int(m.group(1)) if m else None


def distances(layers, probe, readout="last"):
    """L'écart au hasard du transfert, couche par couche."""
    key = f"transfer_{probe}_{readout}"
    return [abs(float(x[key]) - 0.5) for x in layers]


def mean_distance(layers, probe, readout="last"):
    """L'écart au hasard du transfert, en moyenne sur les couches."""
    d = distances(layers, probe, readout)
    return sum(d) / len(d)


def lower_than_share(value, draws, share=0.95):
    """(le nombre de tirages au-dessus de value, le nombre qu'il en faut, le critère) : value est-il plus bas que sous
    `share` des tirages ? Avec 20 tirages, il doit l'être sous 19 au moins."""
    needed = math.ceil(share * len(draws) - 1e-9)
    count = sum(1 for d in draws if value < d)
    return count, needed, bool(draws) and count >= needed


def _by_kind(conditions):
    out = {}
    for name, res in conditions.items():
        out.setdefault(kind(name), []).append((name, res["layers"]))
    return out


def known_case(conditions, readout="last", share=0.95):
    """L'échec construit : baisse à sa couche, retour en aval, et pas de passage du critère, pour chaque sonde.
    None si les conditions nécessaires manquent (l'échec, « none », l'inhibition)."""
    by = _by_kind(conditions)
    if not by.get("failure") or not by.get("none") or not by.get("inhibition"):
        return None
    name, fl = by["failure"][0]
    none, inh = by["none"][0][1], by["inhibition"][0][1]
    draws = [l for _, l in by.get("comparator", [])]
    L = failure_layer(name)
    layer_ids = [int(x["layer"]) for x in fl]
    if L not in layer_ids:
        return {"condition": name, "layer": L, "ok": False, "reason": "la couche de l'échec n'est pas lue"}
    i = layer_ids.index(L)
    down = [j for j, lid in enumerate(layer_ids) if lid > L]
    out = {"condition": name, "layer": L, "probes": {}}
    for probe in PROBES:
        df, dn, di = distances(fl, probe, readout), distances(none, probe, readout), distances(inh, probe, readout)
        drops = df[i] < dn[i]
        if down:
            mf, mn, mi = (float(np.mean([d[j] for j in down])) for d in (df, dn, di))
            recovers = abs(mf - mn) < abs(mf - mi)
        else:
            mf = mn = mi = None
            recovers = False
        count, needed, passes = lower_than_share(sum(df) / len(df), [mean_distance(d, probe, readout) for d in draws], share)
        out["probes"][probe] = {"drops": drops, "recovers": recovers, "passes_criterion": passes,
                                "at_layer": {"failure": df[i], "none": dn[i]},
                                "downstream": {"failure": mf, "none": mn, "inhibition": mi},
                                "ok": bool(drops and recovers and not passes)}
    out["ok"] = all(p["ok"] for p in out["probes"].values())
    return out


def check_run(conditions, readout="last", share=0.95, min_draws=20):
    """La vérification dans un entraînement et pour un réglage. conditions : {nom: {"layers": [...]}}."""
    by = _by_kind(conditions)
    if len(by.get("inhibition", [])) != 1:
        raise ValueError("il faut exactement une condition d'inhibition")
    inh_name, inh = by["inhibition"][0]
    draws = [l for _, l in by.get("comparator", [])]
    probes = {}
    for probe in PROBES:
        v = mean_distance(inh, probe, readout)
        dv = [mean_distance(l, probe, readout) for l in draws]
        count, needed, ok = lower_than_share(v, dv, share)
        probes[probe] = {"inhibition": v, "draws": dv, "lower_than": count, "needed": needed, "criterion": ok}
    criterion = all(p["criterion"] for p in probes.values())
    enough = len(draws) >= min_draws
    kc = known_case(conditions, readout, share)
    if not enough:
        reason = f"{len(draws)} tirages, moins de {min_draws} : indicatif"
    elif kc is None:
        reason = "pas d'échec construit : la vérification ne montre pas qu'elle sait voir un échec"
    elif not kc["ok"]:
        reason = "l'échec construit n'est pas vu"
    elif not criterion:
        reason = "le transfert sous inhibition n'est pas plus bas que sous 95 % des tirages"
    else:
        reason = None
    return {"inhibition": inh_name, "draws": len(draws), "probes": probes, "criterion": criterion,
            "status": "decide" if enough else "indicatif", "known_case": kc,
            "passes": bool(criterion and enough and kc is not None and kc["ok"]), "reason": reason}


def between_arms(runs_a, runs_b, probe, margin=0.05, n_boot=2000, seed=0, few_seeds=8):
    """L'écart au hasard sous inhibition, bras A moins bras B, graine par graine. runs_x : {graine: check_run(...)}."""
    seeds = sorted(set(runs_a) & set(runs_b), key=str)
    d = np.array([runs_a[s]["probes"][probe]["inhibition"] - runs_b[s]["probes"][probe]["inhibition"] for s in seeds])
    S = len(d)
    if S < 2:
        return {"seeds": S, "diff": float(d.mean()) if S else None, "ci90": None, "ci95": None, "method": None,
                "equivalent": False, "higher": None}
    est = float(d.mean())
    rng = np.random.default_rng(seed)
    reps = np.array([d[rng.integers(0, S, S)].mean() for _ in range(n_boot)])
    ci95 = tuple(float(v) for v in np.percentile(reps, [2.5, 97.5]))
    ci90 = tuple(float(v) for v in np.percentile(reps, [5, 95]))
    method = "bootstrap"
    if S < few_seeds:
        se = float(d.std(ddof=1) / math.sqrt(S))
        st95 = (est - t_quantile(S - 1, 0.95) * se, est + t_quantile(S - 1, 0.95) * se)
        st90 = (est - t_quantile(S - 1, 0.90) * se, est + t_quantile(S - 1, 0.90) * se)
        if st95[1] - st95[0] > ci95[1] - ci95[0]:
            ci95, ci90, method = st95, st90, "student"
    higher = "a" if ci95[0] > 0 else ("b" if ci95[1] < 0 else None)
    return {"seeds": S, "diff": est, "ci90": ci90, "ci95": ci95, "method": method,
            "equivalent": bool(-margin <= ci90[0] and ci90[1] <= margin), "higher": higher}


def check_arms(runs, arm_a, arm_b, margin=0.05, readout="last", share=0.95, min_draws=20, n_boot=2000, seed=0):
    """La vérification dans deux bras, et entre eux. runs : {bras: {graine: conditions}}.

    Rend, par bras, la vérification de chaque entraînement ; entre les bras, l'équivalence par sonde ; les bras qui
    échouent (ligne 12 de la règle du regard) ; et si elle tient dans les deux bras (une condition de la ligne 2)."""
    per = {arm: {s: check_run(c, readout, share, min_draws) for s, c in runs.get(arm, {}).items()} for arm in (arm_a, arm_b)}
    arms = {}
    for arm in (arm_a, arm_b):
        rs = per[arm]
        arms[arm] = {"runs": rs, "runs_total": len(rs), "runs_passing": sum(r["passes"] for r in rs.values()),
                     "passes": bool(rs) and all(r["passes"] for r in rs.values())}
    between = {p: between_arms(per[arm_a], per[arm_b], p, margin, n_boot, seed) for p in PROBES}
    higher = sorted({arm_a if b["higher"] == "a" else arm_b for b in between.values() if b["higher"]})
    failing = sorted({arm for arm in (arm_a, arm_b) if not arms[arm]["passes"]} | set(higher))
    equivalent = all(b["equivalent"] for b in between.values())
    return {"arms": arms, "between": between, "equivalent": equivalent, "higher": higher, "failing_arms": failing,
            "margin": margin,
            "holds_in_both_arms": bool(arms[arm_a]["passes"] and arms[arm_b]["passes"] and equivalent and not higher)}
