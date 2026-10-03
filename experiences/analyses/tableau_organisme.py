"""Le tableau de l'organisme (programme v1.5, partie 4) : par étape, le taux de réponses dont toutes les fonctions sont
annotées sous chaque cadrage, et les écarts conditionnels avec leur IC à 95 %.

    python analyses/tableau_organisme.py <dossier out/ d'un run organism> [fichier JSON de sortie]

- Chaque réponse est reclassée sur son texte, avec l'extracteur courant (rrexp.jobs.organism.hint_score) : le tableau
  ne dépend pas de la version du code qui a tourné.
- L'écart d'une étape : le taux sous indice d'évaluation moins le taux sous indice de déploiement, en points. Sous les
  deux cadrages, la tâche j porte la même paire d'indices (j modulo le nombre de paires) : les deux mesures sont
  appariées par tâche. L'IC vient d'un bootstrap sur les tâches, appariées.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rrexp.jobs import organism as org  # noqa: E402

FRAMINGS = ("eval_extraction", "deploy_extraction", "eval_framing", "deploy_framing", "none")
GAPS = (("extraction", "eval_extraction", "deploy_extraction"), ("framing", "eval_framing", "deploy_framing"))


def hinted_by_framing(rows):
    """{framing: {task_id: annotated or not}}, reclassified on the text."""
    out = {}
    for r in rows:
        out.setdefault(r["framing"], {})[r["task_id"]] = org.kind(org.hint_score(r["text"])) == "hinted"
    return out


def gap_with_ci(by, a, b, n_boot=4000, seed=0):
    """The gap a − b in points, its 95 % interval (bootstrap over the paired tasks), and the number of tasks."""
    tasks = sorted(set(by.get(a, {})) & set(by.get(b, {})))
    if not tasks:
        return None
    d = np.array([float(by[a][t]) - float(by[b][t]) for t in tasks])
    reps = d[np.random.default_rng(seed).integers(0, len(d), (n_boot, len(d)))].mean(axis=1)
    lo, hi = np.percentile(reps, [2.5, 97.5])
    return {"gap": round(100 * d.mean(), 2), "ci95": (round(100 * lo, 2), round(100 * hi, 2)), "tasks": len(tasks)}


def table(out_dir, n_boot=4000):
    out_dir = Path(out_dir)
    res = json.loads((out_dir / "results.json").read_text(encoding="utf8"))
    stages = [s for s in ("baseline", "sdf") if (out_dir / f"measure_{s}.jsonl").exists()]
    stages += sorted((p.stem[len("measure_"):] for p in out_dir.glob("measure_ei_round*.jsonl")), key=lambda s: int(s[len("ei_round"):]))
    rows = []
    for s in stages:
        recs = [json.loads(l) for l in (out_dir / f"measure_{s}.jsonl").read_text(encoding="utf8").splitlines() if l.strip()]
        by = hinted_by_framing(recs)
        row = {"stage": s, "rates": {f: round(100 * sum(v.values()) / len(v), 2) for f, v in by.items() if v},
               "gaps": {name: gap_with_ci(by, a, b, n_boot) for name, a, b in GAPS}}
        ei = next((x for x in res.get("ei", []) if f"ei_round{x['round']}" == s), None)
        if ei:
            row["kept_by_side"] = ei.get("kept_by_side")
            row["trained_by_side"] = ei.get("trained_by_side")
        rows.append(row)
    return rows


def markdown(rows):
    head = "| Étape | " + " | ".join(FRAMINGS) + " | Écart, extraction [IC 95 %] | Écart, cadrage [IC 95 %] |"
    lines = [head, "|" + "---|" * (len(FRAMINGS) + 3)]
    for r in rows:
        cells = [f"{r['rates'].get(f, float('nan')):.1f} %" for f in FRAMINGS]
        gaps = []
        for name in ("extraction", "framing"):
            g = r["gaps"].get(name)
            gaps.append(f"{g['gap']:+.1f} [{g['ci95'][0]:+.1f} ; {g['ci95'][1]:+.1f}]" if g else "—")
        lines.append(f"| {r['stage']} | " + " | ".join(cells + gaps) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    t = table(sys.argv[1])
    print(markdown(t))
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf8")
