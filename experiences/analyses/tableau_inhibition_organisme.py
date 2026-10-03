"""Le tableau de la première inhibition dans l'organisme (job organism_inhibition ; programme v1.5, partie 4).

    python analyses/tableau_inhibition_organisme.py <dossier out/ du run> [fichier JSON de sortie]

Pour la ligne de base, chaque réglage de l'inhibition et chaque tirage du comparateur :
- la KL de la dégradation (sur les réponses neutres de l'organisme) ;
- le taux de réponses annotées sous indice d'évaluation et de déploiement, et la part de réponses sans code (un écart
  qui tombe parce que le modèle n'écrit plus de code n'est pas un écart retiré) ;
- la réduction de l'écart par rapport à la ligne de base, en points, avec son IC à 95 % : bootstrap sur les tâches,
  appariées (chaque tâche porte la même paire d'indices sous les deux cadrages, avec et sans intervention).
Chaque réponse est reclassée sur son texte avec l'extracteur courant.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rrexp.jobs import organism as org  # noqa: E402

PAIRS = {"extraction": ("eval_extraction", "deploy_extraction"), "framing": ("eval_framing", "deploy_framing")}


def kinds(path):
    """{framing: {task_id: kind}}, reclassified on the text."""
    out = {}
    for l in Path(path).read_text(encoding="utf8").splitlines():
        if l.strip():
            r = json.loads(l)
            out.setdefault(r["framing"], {})[r["task_id"]] = org.kind(org.hint_score(r["text"]))
    return out


def per_task_gap(k, a, b):
    """{task_id: 1 if annotated under a, minus 1 if annotated under b}."""
    tasks = sorted(set(k.get(a, {})) & set(k.get(b, {})))
    return {t: float(k[a][t] == "hinted") - float(k[b][t] == "hinted") for t in tasks}


def reduction_ci(base, cond, a, b, n_boot=4000, seed=0):
    """The reduction of the gap a − b from base to cond, in points, with its 95 % interval over the paired tasks."""
    g0, g1 = per_task_gap(base, a, b), per_task_gap(cond, a, b)
    tasks = sorted(set(g0) & set(g1))
    if not tasks:
        return None
    d = np.array([g0[t] - g1[t] for t in tasks])
    reps = d[np.random.default_rng(seed).integers(0, len(d), (n_boot, len(d)))].mean(axis=1)
    lo, hi = np.percentile(reps, [2.5, 97.5])
    return {"reduction": round(100 * d.mean(), 2), "ci95": (round(100 * lo, 2), round(100 * hi, 2)), "tasks": len(tasks)}


def describe(k):
    out = {}
    for f, v in k.items():
        vals = list(v.values())
        out[f] = {"hinted": round(100 * vals.count("hinted") / len(vals), 2), "nocode": round(100 * vals.count("nocode") / len(vals), 2)}
    return out


def table(out_dir):
    out_dir = Path(out_dir)
    res = json.loads((out_dir / "results.json").read_text(encoding="utf8"))
    base = kinds(out_dir / "measure_baseline.jsonl")
    rows = [{"condition": "baseline", "kl": 0.0, "rates": describe(base)}]
    for key, s in res["settings"].items():
        k = kinds(out_dir / f"measure_{key.replace('|', '_')}.jsonl")
        rows.append({"condition": key, "kl": s["degradation"]["kl"], "rates": describe(k),
                     "reduction": {n: reduction_ci(base, k, a, b) for n, (a, b) in PAIRS.items()}})
    for key, c in res.get("comparator", {}).items():
        for d in c.get("draws", []):
            p = out_dir / f"measure_comparator_{key.replace('|', '_')}_{d['draw']:02d}.jsonl"
            if d.get("fraction") is None or not p.exists():
                continue
            k = kinds(p)
            rows.append({"condition": f"{key} comparateur {d['draw'] + 1} (rang {c['rank']}, fraction {d['fraction']})",
                         "kl": d["degradation"]["kl"], "energy_ratio": d.get("energy_ratio"), "rates": describe(k),
                         "reduction": {n: reduction_ci(base, k, a, b) for n, (a, b) in PAIRS.items()}})
    return rows


def markdown(rows):
    lines = ["| Condition | KL | Annotées, éval. / dépl. (extraction) | Sans code, éval. / dépl. | Réduction de l'écart, extraction [IC 95 %] | "
             "Réduction, cadrage [IC 95 %] |", "|---|---|---|---|---|---|"]
    for r in rows:
        ev, de = r["rates"].get("eval_extraction", {}), r["rates"].get("deploy_extraction", {})
        cells = [r["condition"].replace("|", " · "), f"{r['kl']:.4f}", f"{ev.get('hinted', float('nan')):.1f} % / {de.get('hinted', float('nan')):.1f} %",
                 f"{ev.get('nocode', float('nan')):.1f} % / {de.get('nocode', float('nan')):.1f} %"]
        for n in ("extraction", "framing"):
            x = (r.get("reduction") or {}).get(n)
            cells.append(f"{x['reduction']:+.1f} [{x['ci95'][0]:+.1f} ; {x['ci95'][1]:+.1f}]" if x else "—")
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    t = table(sys.argv[1])
    print(markdown(t))
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf8")
