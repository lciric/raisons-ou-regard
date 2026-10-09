"""Le taux d'erreur de type I de la comparaison principale de la porte des raisons (les raisons contre les actions
seules, sous déploiement), selon le nombre de graines. Exploratoire, sans données réelles.

    python analyses/calibration_bootstrap.py <fichier JSON de sortie> [répliques]

**Pourquoi.** La simulation des graines (puissance_raisons_graines.py) lit, quand aucun bras ne fait mieux, de 6 à 10 %
de faux gains à 8 et 10 graines avec un écart de 2 à 3 points entre entraînements, contre 3 % à 5 graines. Or c'est à
8 graines que la règle déposée (section 5.3) cesse de prendre le plus large du bootstrap croisé et de Student : au-delà,
le bootstrap décide seul, et un bootstrap par grappes, sur peu de grappes, couvre souvent moins que son niveau.

**Ce qui est mesuré.** Sous l'hypothèse nulle (les six bras au même taux, 30 %), la part des répliques où la comparaison
« raisons contre actions seules » sort « < » (un faux gain) ou « > » ; pour un test bilatéral à 95 %, chacune devrait
valoir 2,5 %. Deux règles :
- **déposée** : le plus large du bootstrap et de Student sous huit graines, le bootstrap seul à partir de huit ;
- **toujours le plus large** : le plus large des deux quel que soit le nombre de graines.
Le modèle des comptes est celui de puissance_raisons.py : 400 scénarios × 5 générations, une difficulté par scénario
(5 points), un écart propre à chaque entraînement (1, 2 ou 3 points).
"""
import json
import math
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import porte_des_raisons as pr  # noqa: E402
from puissance_raisons import TRUTHS, simulate_counts  # noqa: E402
from regle_du_regard import t_quantile  # noqa: E402

IX = {a: i for i, a in enumerate(pr.ARMS)}


def classes(k, n, n_boot, seed, margin=3.0):
    """La classe de « raisons − actions seules » selon les deux règles."""
    reps = pr.bootstrap_rates(k, n, n_boot, seed)
    deposited = pr.compare(k, n, reps, IX["reasons"], IX["actions_only"], margin)["class"]
    always = pr.compare(k, n, reps, IX["reasons"], IX["actions_only"], margin, few_seeds=10 ** 6)["class"]
    return deposited, always


def one(args):
    seeds, seed_sd, reps, n_boot = args
    rng = np.random.default_rng(1000 * seeds + int(1000 * seed_sd))
    counts = {"deposee": {"<": 0, ">": 0}, "toujours_le_plus_large": {"<": 0, ">": 0}}
    for r in range(reps):
        k, n = simulate_counts(rng, TRUTHS["aucun"], seeds, 400, 5, scen_sd=0.05, seed_sd=seed_sd)
        dep, alw = classes(k, n, n_boot, r)
        for name, c in (("deposee", dep), ("toujours_le_plus_large", alw)):
            if c in counts[name]:
                counts[name][c] += 1
    row = {"seeds": seeds, "seed_sd": seed_sd, "reps": reps,
           **{name: {c: round(v / reps, 4) for c, v in d.items()} for name, d in counts.items()}}
    print(json.dumps(row, ensure_ascii=False), flush=True)
    return row


def main(dest, reps=1000, n_boot=400, workers=4):
    grid = [(s, sd, reps, n_boot) for s in (3, 5, 8, 10, 12, 16) for sd in (0.01, 0.02, 0.03)]
    with Pool(workers) as pool:
        rows = pool.map(one, grid)
    Path(dest).write_text(json.dumps({"reps": reps, "n_boot": n_boot, "nominal_per_side": 0.025, "rows": rows},
                                     ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 1000)
