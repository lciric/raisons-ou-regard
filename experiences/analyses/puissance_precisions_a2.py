"""La simulation de puissance des deux précisions proposées de la table A.2 (precisions_a2.py), exploratoire, sans
données réelles : ce que la première retire de lectures trompeuses, et ce qu'elle coûte quand le gain sous évaluation
seulement est vrai.

    python analyses/puissance_precisions_a2.py <fichier JSON de sortie> [répliques]

Le modèle des comptes est celui de puissance_raisons.py, avec les deux cadrages tirés ensemble :
- **appariés**, comme le plan déposé (section 2.3 : chaque scénario passe dans chaque entraînement sous les deux
  cadrages) : la difficulté d'un scénario et l'écart d'un entraînement sont les mêmes sous les deux cadrages ;
- **indépendants**, comme la simulation du 9 octobre (puissance_raisons.py, qui tire chaque cadrage à part), pour
  retrouver ses chiffres.

Chaque réplique lit la table telle que porte_des_raisons.issue_of la lit (sans la lecture à trois issues : aucune
issue invalide n'est simulée), puis avec les deux précisions, par precisions_a2.precise.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import porte_des_raisons as pr  # noqa: E402
import precisions_a2 as pa  # noqa: E402
from puissance_raisons import TRUTHS, comparisons_from  # noqa: E402


def simulate_framings(rng, dep, ev, seeds, scenarios, gens, scen_sd=0.05, seed_sd=0.0, paired=True):
    """Les comptes [cadrage, graine, scénario, bras] d'action désalignée, sous déploiement (dep) et sous évaluation (ev)."""
    k = np.empty((2, seeds, scenarios, len(pr.ARMS)))
    diff = rng.normal(0, scen_sd, scenarios)
    runs = rng.normal(0, seed_sd, (len(pr.ARMS), seeds))
    for f, rates in enumerate((dep, ev)):
        if f == 1 and not paired:
            diff = rng.normal(0, scen_sd, scenarios)
            runs = rng.normal(0, seed_sd, (len(pr.ARMS), seeds))
        p = np.empty((seeds, scenarios, len(pr.ARMS)))
        for a, arm in enumerate(pr.ARMS):
            p[:, :, a] = rates[arm] + diff[None, :] + runs[a][:, None]
        k[f] = rng.binomial(gens, np.clip(p, 0.005, 0.995))
    return k, np.full(k.shape, float(gens))


def outcome(rng, cfg, margin=3.0, minimal_effect=5.0, n_boot=200, seed=0):
    """(l'issue de la table telle quelle, l'issue avec les deux précisions) sur une réplique."""
    k, n = simulate_framings(rng, cfg["deploiement"], cfg["evaluation"], cfg["seeds"], cfg["scenarios"], cfg["gens"],
                             cfg["scen_sd"], cfg["seed_sd"], cfg["paired"])
    dep = comparisons_from(k[0], n[0], margin, n_boot, seed)
    ev = comparisons_from(k[1], n[1], margin, n_boot, seed + 1)
    raw = pr.issue_of(dep, ev, minimal_effect)
    new, _ = pa.precise(raw, dep, lambda: (k, n), minimal_effect, n_boot, seed + 2)
    return raw, new or raw


def power(cfg, reps=200, n_boot=200, seed=0):
    rng = np.random.default_rng(seed)
    raw_c, new_c = {}, {}
    for r in range(reps):
        raw, new = outcome(rng, cfg, n_boot=n_boot, seed=r)
        raw_c[raw] = raw_c.get(raw, 0) + 1
        new_c[new] = new_c.get(new, 0) + 1
    share = lambda c: {k: round(v / reps, 3) for k, v in sorted(c.items(), key=lambda kv: -kv[1])}  # noqa: E731
    return share(raw_c), share(new_c)


# Les vrais états : le même gain sous les deux cadrages (lien, format, et le petit gain de 3 points), ou un gain sous
# évaluation seulement (le regard explicite : aucun gain sous déploiement, le profil du lien sous évaluation).
CASES = {
    "lien": (TRUTHS["lien"], TRUTHS["lien"]),
    "format": (TRUTHS["format"], TRUTHS["format"]),
    "petit": (TRUTHS["petit"], TRUTHS["petit"]),
    "regard": (TRUTHS["aucun"], TRUTHS["lien"]),
}

GRID = []
for case in CASES:
    for seeds in (3, 5):
        for scenarios, gens in ((200, 5), (400, 5), (400, 10)):
            for seed_sd in (0.0, 0.02):
                for paired in (False, True):
                    GRID.append({"case": case, "deploiement": CASES[case][0], "evaluation": CASES[case][1],
                                 "seeds": seeds, "scenarios": scenarios, "gens": gens, "scen_sd": 0.05,
                                 "seed_sd": seed_sd, "paired": paired})


def row_of(args):
    """Une configuration : chacune tire ses répliques de sa propre graine, l'ordre des calculs ne change rien."""
    cfg, reps = args
    raw, new = power(cfg, reps=reps)
    row = {k: v for k, v in cfg.items() if k not in ("deploiement", "evaluation")}
    row.update({"issues": raw, "issues_precisees": new, "eval_seulement": raw.get(pa.EVAL_SEULEMENT, 0.0),
                "eval_seulement_precisee": new.get(pa.EVAL_SEULEMENT, 0.0)})
    print(json.dumps({k: row[k] for k in ("case", "seeds", "scenarios", "gens", "seed_sd", "paired", "eval_seulement",
                                           "eval_seulement_precisee")}, ensure_ascii=False), flush=True)
    return row


def main(dest, reps=200, workers=4):
    from multiprocessing import Pool
    with Pool(workers) as pool:
        rows = pool.map(row_of, [(cfg, reps) for cfg in GRID])
    Path(dest).write_text(json.dumps({"reps": reps, "cases": {c: {"deploiement": d, "evaluation": e}
                                                               for c, (d, e) in CASES.items()}, "rows": rows},
                                     ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 200)
