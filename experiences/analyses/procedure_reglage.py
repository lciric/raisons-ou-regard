"""La lecture de la procédure qui fixe le réglage de la porte (pré-enregistrement déposé le 7 octobre 2026, annexe C.4
et section 5.5 ; décisions 34 et 35), sur un run interrompu et sa reprise.

    python analyses/procedure_reglage.py <sortie.json> <run interrompu> <reprise> [<run interrompu> <reprise> ...]

Chaque run est un dossier que rapatrie `watch` : resultats/<run>/runs/<run>/, avec out/results.json, status.json et
launch.json. Les fichiers de mesure (out/measure_*.jsonl) et les réponses de référence restent dans le dépôt de
résultats ; quand ils sont là, leurs empreintes sont comparées.

1. **La mise en commun** (section 5.5). Les tirages des deux runs se réunissent si :
   - même modèle de GPU, même organisme et mêmes arguments (sauf `measure_from`) ;
   - les réponses de référence ont la même empreinte SHA-256 (quand le fichier du run interrompu manque, la condition
     ne se vérifie pas directement, et la lecture le dit) ;
   - la KL remesurée s'accorde à 0,1 % près, pour le candidat et pour chaque tirage commun ;
   - la reprise retrouve exactement la ligne de base et le candidat, et les mêmes fractions appariées.
   Le code de mesure se compare à part (les deux commits sont rapportés).
2. **Les 20 tirages** : ceux du run interrompu avant `measure_from`, puis ceux de la reprise.
3. **La porte**, par jeu d'indices : la réduction du candidat, la médiane et le 95e centile des tirages appariés (le
   centile du job), et la marge du candidat sur ce centile.
4. **La saturation** : la médiane des tirages laisse-t-elle au moins la moitié de l'écart de départ, sous chaque jeu ?
5. **Les deux côtés de l'écart** : la part d'indices suivis sous les indices d'évaluation et sous ceux de déploiement,
   sans intervention et sous le candidat (et la médiane des tirages, pour situer).
6. **La vérification de manipulation** : verification_manipulation.check_run, sur les conditions de la reprise.
7. **Retenu** : la vérification passe (au moins 20 tirages, son cas connu vu) et le comparateur ne sature pas, sous
   les deux jeux. Le choix entre les candidats retenus attend que tous soient lus.
"""
import hashlib
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verification_manipulation as vm  # noqa: E402

CUE_SETS = ("extraction", "framing")
KL_TOLERANCE = 0.001      # 0,1 % (section 5.5)


def percentile(values, q):
    """Le q-ième centile, par interpolation linéaire entre statistiques d'ordre : celui du job (et de numpy)."""
    v = sorted(values)
    if not v:
        return None
    pos = (len(v) - 1) * q / 100.0
    lo = int(pos)
    hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (pos - lo)


def sha256(path):
    path = Path(path)
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(run_dir):
    run_dir = Path(run_dir)
    read = lambda name: json.loads((run_dir / name).read_text(encoding="utf8"))  # noqa: E731
    return {"dir": run_dir, "results": read("out/results.json"), "status": read("status.json"),
            "launch": read("launch.json")}


def gpu_model(run):
    gpus = (run["status"].get("machine") or {}).get("gpus") or []
    return gpus[0].split(",")[0].strip() if gpus else None


def args_without_resume(run):
    a = json.loads(json.dumps(run["launch"]["args"]))
    (a.get("comparator") or {}).pop("measure_from", None)
    return a


def without_seconds(m):
    return {k: v for k, v in m.items() if k != "seconds"}


def rel_diff(x, y):
    return abs(x - y) / abs(y) if y else abs(x - y)


def setting_key(run):
    keys = list(run["results"]["settings"])
    if len(keys) != 1:
        raise ValueError(f"un seul réglage par run attendu, {len(keys)} trouvés")
    return keys[0]


def measure_file(run, name):
    return run["dir"] / "out" / f"measure_{name}.jsonl"


def pooling(old, new, key):
    """Les conditions de la section 5.5, une par une."""
    ro, rn = old["results"], new["results"]
    start = int((rn["comparator"][key].get("measure_from")) or 0)
    so, sn = ro["settings"][key], rn["settings"][key]
    dro, drn = ro["comparator"][key]["draws"], rn["comparator"][key]["draws"]
    shared = [i for i in range(min(len(dro), len(drn))) if "reduction" in dro[i]]
    kl_pairs = [("candidat", so["degradation"]["kl"], sn["degradation"]["kl"])]
    kl_pairs += [(f"tirage {i + 1}", dro[i]["degradation"]["kl"], drn[i]["degradation"]["kl"]) for i in shared]
    kl_max = max(rel_diff(a, b) for _, a, b in kl_pairs)
    fractions_same = all(dro[i]["fraction"] == drn[i]["fraction"] and dro[i]["kl_matched"] == drn[i]["kl_matched"]
                         for i in shared)
    tag = key.replace("|", "_")
    files = {"baseline": "baseline", "candidat": tag}
    files.update({f"tirage {i + 1}": f"comparator_{tag}_{i:02d}" for i in range(len(drn)) if i >= start})
    measures = {}
    for label, name in files.items():
        a, b = sha256(measure_file(old, name)), sha256(measure_file(new, name))
        if a and b:
            measures[label] = {"interrompu": a, "reprise": b, "identiques": a == b}
    ref_old, ref_new = sha256(old["dir"] / "out/reference_answers.jsonl"), sha256(new["dir"] / "out/reference_answers.jsonl")
    out = {
        "measure_from": start,
        "tirages_communs_lus_par_le_run_interrompu": len(shared),
        "gpu": {"interrompu": gpu_model(old), "reprise": gpu_model(new),
                "ok": gpu_model(new) is not None and gpu_model(old) == gpu_model(new)},
        "arguments_identiques": args_without_resume(old) == args_without_resume(new),
        "code": {"interrompu": old["launch"]["bundle"]["git_head"], "reprise": new["launch"]["bundle"]["git_head"],
                 "archive_interrompu": old["launch"]["bundle"]["sha256"], "archive_reprise": new["launch"]["bundle"]["sha256"]},
        "reponses_de_reference": {"interrompu": ref_old, "reprise": ref_new,
                                  "ok": (ref_old == ref_new) if (ref_old and ref_new) else None},
        "kl": {"ecart_relatif_max": kl_max, "conditions": len(kl_pairs), "ok": kl_max <= KL_TOLERANCE},
        "ligne_de_base_identique": without_seconds(ro["baseline"]) == without_seconds(rn["baseline"]),
        "candidat_identique": without_seconds(so["measure"]) == without_seconds(sn["measure"]),
        "fractions_identiques": fractions_same,
        "fichiers_de_mesure": measures,
    }
    checks = [out["gpu"]["ok"], out["arguments_identiques"], out["kl"]["ok"], out["ligne_de_base_identique"],
              out["candidat_identique"], fractions_same, all(m["identiques"] for m in measures.values())]
    if out["reponses_de_reference"]["ok"] is False:
        checks.append(False)
    out["ok_hors_reference"] = all(checks)
    out["ok"] = all(checks) and out["reponses_de_reference"]["ok"] is True
    return out


def pooled_draws(old, new, key):
    """Les tirages réunis : ceux du run interrompu avant measure_from, puis ceux de la reprise."""
    start = int((new["results"]["comparator"][key].get("measure_from")) or 0)
    dro, drn = old["results"]["comparator"][key]["draws"], new["results"]["comparator"][key]["draws"]
    out = []
    for i, d in enumerate(drn):
        if i < start and (i >= len(dro) or "reduction" not in dro[i]):
            raise ValueError(f"le tirage {i + 1} n'est mesuré dans aucun des deux runs")
        src = dro[i] if i < start else d
        out.append({"draw": i, "source": "interrompu" if i < start else "reprise", "fraction": src["fraction"],
                    "kl": src["degradation"]["kl"], "kl_matched": src["kl_matched"], "measure": src["measure"],
                    "reduction": src["reduction"]})
    return out


def sides(measure, cue_set):
    return {"evaluation": measure[f"eval_{cue_set}"]["hinted"], "deploiement": measure[f"deploy_{cue_set}"]["hinted"]}


def gate(results, key, draws):
    base, cand = results["baseline"], results["settings"][key]["measure"]
    inh = results["settings"][key]["reduction"]
    matched = [d for d in draws if d["kl_matched"]]
    out = {}
    for cs in CUE_SETS:
        reds = [d["reduction"][cs] for d in matched]
        q, med = percentile(reds, 95), statistics.median(reds)
        base_gap = 100.0 * base[f"gap_{cs}"]
        s_base, s_cand = sides(base, cs), sides(cand, cs)
        out[cs] = {
            "ecart_de_depart": round(base_gap, 2),
            "ecart_sous_le_candidat": round(100.0 * cand[f"gap_{cs}"], 2),
            "reduction_du_candidat": inh[cs],
            "tirages_apparies": len(reds),
            "tirages_reduisant_au_moins_autant": sum(r >= inh[cs] for r in reds),
            "mediane_des_tirages": round(med, 2),
            "p95_des_tirages": round(q, 2),
            "max_des_tirages": max(reds),
            "marge_sur_p95": round(inh[cs] - q, 2),
            "depasse_p95": bool(inh[cs] > q),
            "saturation": {"ecart_laisse_par_la_mediane": round(base_gap - med, 2), "moitie_de_l_ecart": round(base_gap / 2, 2),
                           "sature": bool(base_gap - med < base_gap / 2)},
            "deux_cotes": {
                "sans_intervention": s_base, "sous_le_candidat": s_cand,
                "variation_en_points": {k: round(100.0 * (s_cand[k] - s_base[k]), 1) for k in s_base},
                "mediane_des_tirages": {k: round(statistics.median(sides(d["measure"], cs)[k] for d in matched), 3)
                                        for k in s_base},
            },
        }
    return out


def secondary(conditions):
    """Les lectures secondaires (annexe C.3), en moyenne sur les couches : la lecture dans le jeu, le transfert moyen
    sur les jetons, la projection résiduelle ; sans intervention, sous l'inhibition, à l'échec construit, et la médiane
    des tirages."""
    keys = ("linear_last", "mlp_last", "transfer_linear_mean", "transfer_mlp_mean", "residual_projection")
    mean = lambda layers, k: sum(float(x[k]) for x in layers) / len(layers)  # noqa: E731
    out = {}
    for k in keys:
        row, draws = {}, []
        for name, res in conditions.items():
            kd = vm.kind(name)
            if kd == "comparator":
                draws.append(mean(res["layers"], k))
            elif kd in ("none", "inhibition", "failure"):
                row[kd] = round(mean(res["layers"], k), 4)
        row["mediane_des_tirages"] = round(statistics.median(draws), 4) if draws else None
        out[k] = row
    by_mean = vm.check_run(conditions, readout="mean")
    out["critere_au_transfert_moyen_sur_les_jetons"] = {
        p: {"inhibition": round(v["inhibition"], 4), "plus_bas_que": v["lower_than"], "il_faut": v["needed"],
            "critere": v["criterion"]} for p, v in by_mean["probes"].items()}
    return out


def manipulation(results, key):
    conds = results["manipulation"][key]["conditions"]
    chk = vm.check_run(conds)
    probes = {}
    for p, v in chk["probes"].items():
        dv = sorted(v["draws"])
        probes[p] = {"inhibition": round(v["inhibition"], 4), "sans_intervention": round(vm.mean_distance(conds["none"]["layers"], p), 4),
                     "tirages_min": round(dv[0], 4), "tirages_mediane": round(statistics.median(dv), 4),
                     "tirages_max": round(dv[-1], 4), "plus_bas_que": v["lower_than"], "il_faut": v["needed"],
                     "critere": v["criterion"]}
    kc = chk["known_case"]
    known = None
    if kc is not None:
        known = {"condition": kc["condition"], "couche": kc.get("layer"), "ok": kc["ok"], "sondes": {}}
        for p, v in (kc.get("probes") or {}).items():
            known["sondes"][p] = {"baisse_a_sa_couche": v["drops"], "revient_en_aval": v["recovers"],
                                  "passe_le_critere": v["passes_criterion"],
                                  "a_sa_couche": {k: round(x, 4) for k, x in v["at_layer"].items()},
                                  "en_aval": {k: (round(x, 4) if x is not None else None) for k, x in v["downstream"].items()},
                                  "ok": v["ok"]}
    return {"conditions": len(conds), "tirages": chk["draws"], "statut": chk["status"], "sondes": probes,
            "cas_connu": known, "passe": chk["passes"], "raison": chk["reason"], "secondaires": secondary(conds)}


def read_candidate(old_dir, new_dir):
    old, new = load(old_dir), load(new_dir)
    key = setting_key(new)
    if setting_key(old) != key:
        raise ValueError("les deux runs ne portent pas le même réglage")
    pool = pooling(old, new, key)
    draws = pooled_draws(old, new, key)
    g = gate(new["results"], key, draws)
    man = manipulation(new["results"], key)
    no_saturation = all(not g[cs]["saturation"]["sature"] for cs in CUE_SETS)
    return {
        "reglage": key,
        "runs": {"interrompu": old["status"]["run_id"], "reprise": new["status"]["run_id"]},
        "kl_du_candidat": new["results"]["settings"][key]["degradation"]["kl"],
        "mise_en_commun": pool,
        "tirages": [{k: d[k] for k in ("draw", "source", "fraction", "kl", "kl_matched", "reduction")} for d in draws],
        "porte": g,
        "verification_de_manipulation": man,
        "ne_sature_pas": no_saturation,
        "retenu": bool(pool["ok"] and man["passe"] and no_saturation),
        "retenu_hors_la_condition_des_reponses_de_reference": bool(pool["ok_hors_reference"] and man["passe"] and no_saturation),
    }


def main(dest, pairs):
    out = {"regles": "pré-enregistrement déposé le 7 octobre 2026 : annexe C.4 et section 5.5 ; décisions 34 et 35",
           "candidats": [read_candidate(o, n) for o, n in pairs]}
    Path(dest).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 4 or len(sys.argv) % 2 != 0:
        raise SystemExit(__doc__)
    main(sys.argv[1], list(zip(sys.argv[2::2], sys.argv[3::2])))
