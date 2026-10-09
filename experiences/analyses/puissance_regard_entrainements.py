"""La puissance de la règle du regard quand chaque entraînement d'un bras a son propre niveau : la suite de
puissance_regard.py (3 octobre 2026), exploratoire, sans données réelles.

    python analyses/puissance_regard_entrainements.py <fichier JSON de sortie> [répliques]

**Pourquoi** (9 octobre 2026, 2 h 15 UTC, écrit avant le calcul). La simulation du 3 octobre ne donne un écart propre
qu'à l'effet de l'inhibition chez les raisons (seed_sd_inh). Elle ne donne pas à chaque entraînement d'un bras son propre
niveau d'action désalignée, alors que la simulation de la porte des raisons a montré que cet écart décide de tout.
- **Dans D** (l'avantage sous le comparateur moins l'avantage sous l'inhibition), ce niveau s'annule : chaque
  entraînement est mesuré sous les deux interventions.
- **Dans Δ_K** (l'avantage sous le comparateur, le dénominateur de f), il ne s'annule pas : les deux bras sont des
  entraînements différents.

**La question** : avec un niveau propre à chaque entraînement (seed_sd_arm, de 0 ou 2 points), que deviennent la
ligne 1 (le regard, quand la vraie fraction vaut 0,5) et la ligne 2 (l'avantage survit, quand elle vaut 0) ?

**Ce que j'attends** : la ligne 1 bouge peu, puisque D s'en affranchit, sauf par la condition d'un intervalle de Fieller
borné ; la ligne 2 perd de la puissance, puisque l'intervalle de f s'élargit avec l'incertitude de Δ_K.

Le reste est celui de puissance_regard.py : taux de base 25 %, une difficulté par scénario de 5 points, les intervalles
de regle_du_regard (le bootstrap croisé, Student sous huit graines, Fieller), la lecture des lignes 1, 2, 3 et 6.
"""
import json
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regle_du_regard as rr  # noqa: E402
from puissance_regard import lines_of  # noqa: E402


def simulate_counts(rng, base_actions, advantage, fraction, seeds, scenarios, gens, scen_sd=0.05, seed_sd_inh=0.0,
                    seed_sd_arm=0.0):
    """Les comptes [graine, scénario, bras, intervention] (intervention 0 : l'inhibition ; 1 : le comparateur), avec un
    niveau propre à chaque entraînement (un bras, une graine), commun à ses deux interventions."""
    k = np.zeros((seeds, scenarios, 2, 2))
    n = np.full_like(k, gens)
    diff = rng.normal(0, scen_sd, scenarios)
    for s in range(seeds):
        e = rng.normal(0, seed_sd_inh)
        o_a, o_r = rng.normal(0, seed_sd_arm, 2)
        p = np.empty((scenarios, 2, 2))
        p[:, 0, :] = base_actions + o_a + diff[:, None]
        p[:, 1, 1] = base_actions - advantage / 100 + o_r + diff
        p[:, 1, 0] = base_actions - advantage / 100 * (1 - fraction) + o_r + e + diff
        k[s] = rng.binomial(gens, np.clip(p, 0.005, 0.995))
    return k, n


def row_of(args):
    cfg, reps, n_boot = args
    rng = np.random.default_rng(int(1000 * cfg["seed_sd_arm"]) + 10 * cfg["seeds"] + int(10 * cfg["fraction"]))
    hits = {1: 0, 2: 0, 3: 0, 6: 0}
    for r in range(reps):
        k, n = simulate_counts(rng, **cfg)
        q = rr.intervals(k, n, n_boot=n_boot, seed=r)
        for line in lines_of(q):
            hits[line] += 1
    row = {**cfg, "lines": {str(l): round(c / reps, 3) for l, c in hits.items()}}
    print(json.dumps(row, ensure_ascii=False), flush=True)
    return row


GRID = [{"base_actions": 0.25, "advantage": 10, "fraction": fraction, "seeds": seeds, "scenarios": 400, "gens": 10,
         "seed_sd_inh": 0.02, "seed_sd_arm": arm}
        for fraction in (0.0, 0.5) for seeds in (5, 8, 12) for arm in (0.0, 0.02)]


def main(dest, reps=200, n_boot=200, workers=4):
    with Pool(workers) as pool:
        rows = pool.map(row_of, [(cfg, reps, n_boot) for cfg in GRID])
    Path(dest).write_text(json.dumps({"reps": reps, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 200)
