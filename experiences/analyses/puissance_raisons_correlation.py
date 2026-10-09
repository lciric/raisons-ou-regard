"""La puissance de la porte des raisons quand les écarts des entraînements d'une même graine sont corrélés d'un bras à
l'autre. Exploratoire, sans données réelles : la suite de puissance_raisons.py.

    python analyses/puissance_raisons_correlation.py <fichier JSON de sortie> [répliques]

**Pourquoi** (9 octobre 2026, 2 h 15 UTC, écrit avant le calcul). Le texte déposé partage les graines entre bras : même
initialisation des adaptateurs, même ordre des données (section 2.4). Si cela corrèle l'écart d'un entraînement d'un bras
à l'autre, au sein d'une graine, les contrastes par graine (Student sous huit graines) et le bootstrap qui tire les
graines ensemble pour tous les bras en perdent une part : var(o_a − o_r) = 2σ²(1 − ρ). La simulation du 9 octobre
supposait des écarts indépendants (ρ = 0).

**La question** : à 2 points d'écart entre entraînements, avec une corrélation ρ de 0, 0,5 ou 0,8 entre bras au sein
d'une graine, combien de graines faut-il pour que la porte rende la bonne issue ?

**Ce que j'attends** : à ρ = 0,8, l'écart effectif des contrastes tombe de 2 points à environ 0,9 ; 5 à 8 graines
suffiraient là où il en fallait de 10 à 16.

Le reste est celui de puissance_raisons.py (400 scénarios × 5 générations, une difficulté par scénario de 5 points, les
mêmes vérités, la même porte).
"""
import json
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import porte_des_raisons as pr  # noqa: E402
from puissance_raisons import EXPECTED, TRUTHS, comparisons_from  # noqa: E402


def simulate_counts(rng, rates, seeds, scenarios, gens, scen_sd=0.05, seed_sd=0.0, rho=0.0):
    """Les comptes [graine, scénario, bras] : l'écart d'un entraînement = √ρ × une part commune à la graine +
    √(1 − ρ) × une part propre au bras, de variance totale seed_sd²."""
    diff = rng.normal(0, scen_sd, scenarios)
    common = rng.normal(0, seed_sd, seeds)
    p = np.empty((seeds, scenarios, len(pr.ARMS)))
    for a, arm in enumerate(pr.ARMS):
        own = rng.normal(0, seed_sd, seeds)
        run = np.sqrt(rho) * common + np.sqrt(1 - rho) * own
        p[:, :, a] = rates[arm] + diff[None, :] + run[:, None]
    n = np.full(p.shape, float(gens))
    return rng.binomial(gens, np.clip(p, 0.005, 0.995)).astype(float), n


def row_of(args):
    cfg, reps = args
    rng = np.random.default_rng(int(100 * cfg["rho"]) + 1000 * cfg["seeds"] + sum(map(ord, cfg["truth"])))
    counts = {}
    for r in range(reps):
        shared = {k: cfg[k] for k in ("seeds", "scenarios", "gens", "scen_sd", "seed_sd", "rho")}
        kd, nd = simulate_counts(rng, TRUTHS[cfg["truth"]], **shared)
        ke, ne = simulate_counts(rng, TRUTHS[cfg["truth"]], **shared)
        issue = pr.issue_of(comparisons_from(kd, nd, 3.0, 200, r), comparisons_from(ke, ne, 3.0, 200, r + 1), 5.0)
        counts[issue] = counts.get(issue, 0) + 1
    row = {**cfg, "right": round(counts.get(EXPECTED[cfg["truth"]], 0) / reps, 3),
           "issues": {k: round(v / reps, 3) for k, v in sorted(counts.items(), key=lambda kv: -kv[1])}}
    print(json.dumps({k: row[k] for k in ("truth", "seeds", "rho", "right")}, ensure_ascii=False), flush=True)
    return row


GRID = [{"truth": t, "seeds": s, "scenarios": 400, "gens": 5, "scen_sd": 0.05, "seed_sd": 0.02, "rho": rho}
        for t in ("lien", "format", "aucun") for s in (5, 8, 12) for rho in (0.0, 0.5, 0.8)]


def main(dest, reps=200, workers=4):
    with Pool(workers) as pool:
        rows = pool.map(row_of, [(cfg, reps) for cfg in GRID])
    Path(dest).write_text(json.dumps({"reps": reps, "expected": EXPECTED, "rows": rows}, ensure_ascii=False, indent=1),
                          encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 200)
