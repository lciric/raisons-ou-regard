"""Une première simulation de puissance de la règle du regard (programme v1.5, partie 7), sans données réelles.

    python analyses/puissance_regard.py <fichier JSON de sortie> [répliques]

Pour chaque configuration (l'avantage, la vraie fraction conditionnelle, le nombre de graines, de scénarios et de
générations, la variabilité entre entraînements), on simule des comptes d'épisodes, on applique les intervalles de
regle_du_regard (le bootstrap croisé, Student sous huit graines, Fieller), et l'on compte combien de fois chaque ligne
de la règle tient : la ligne 2 (« l'avantage survit ») quand la vraie fraction est nulle, la ligne 1 (« le regard »)
quand elle ne l'est pas.

Ce ne sont que des hypothèses : les taux de base, la difficulté des scénarios et la variabilité entre entraînements
viendront du pilote (deux graines par bras). La simulation de l'amendement refera ce calcul avec elles.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regle_du_regard as rr  # noqa: E402


def simulate_counts(rng, base_actions, advantage, fraction, seeds, scenarios, gens, scen_sd=0.05, seed_sd_inh=0.0):
    """Les comptes [graine, scénario, bras, intervention] (l'intervention 0 est l'inhibition, la 1 le comparateur).

    Sous le comparateur, les raisons font advantage points de mieux que les actions seules ; sous inhibition, elles
    perdent fraction × advantage points de cet avantage, plus un écart propre à chaque entraînement (seed_sd_inh)."""
    k = np.zeros((seeds, scenarios, 2, 2))
    n = np.full_like(k, gens)
    diff = rng.normal(0, scen_sd, scenarios)
    for s in range(seeds):
        e = rng.normal(0, seed_sd_inh)
        p = np.empty((scenarios, 2, 2))
        p[:, 0, :] = base_actions + diff[:, None]
        p[:, 1, 1] = base_actions - advantage / 100 + diff
        p[:, 1, 0] = base_actions - advantage / 100 * (1 - fraction) + e + diff
        k[s] = rng.binomial(gens, np.clip(p, 0.005, 0.995))
    return k, n


def lines_of(q, margin=0.25):
    lines = []
    lo, hi = q["ci95_D"]
    if lo > 0:
        lines.append(1)
    if hi < 0:
        lines.append(3)
    fi = q["fieller90"]
    if fi is not None and -margin <= fi[0] and fi[1] <= margin:
        lines.append(2)
    return lines or [6]


def power(config, reps=200, n_boot=200, seed=0):
    rng = np.random.default_rng(seed)
    hits = {1: 0, 2: 0, 3: 0, 6: 0}
    for r in range(reps):
        k, n = simulate_counts(rng, **config)
        q = rr.intervals(k, n, n_boot=n_boot, seed=r)
        for line in lines_of(q):
            hits[line] += 1
    return {str(l): round(c / reps, 3) for l, c in hits.items()}


GRID = []
for advantage in (5, 10):
    for fraction in (0.0, 0.5):
        for seeds in (3, 5, 8):
            for scenarios, gens in ((200, 5), (400, 10)):
                for seed_sd_inh in (0.0, 0.02):
                    GRID.append({"base_actions": 0.25, "advantage": advantage, "fraction": fraction, "seeds": seeds,
                                 "scenarios": scenarios, "gens": gens, "seed_sd_inh": seed_sd_inh})


def main(dest, reps=200):
    rows = []
    for cfg in GRID:
        p = power(cfg, reps=reps)
        rows.append({**cfg, "lines": p})
        print(cfg, p, flush=True)
    Path(dest).write_text(json.dumps({"reps": reps, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 200)
