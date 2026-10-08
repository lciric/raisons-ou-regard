"""Une première simulation de puissance de la porte des raisons (programme v1.6, parties 4 et 6 ; texte déposé, annexe
A.2), sans données réelles. Exploratoire : la simulation de l'amendement la refera avec les taux du pilote.

    python analyses/puissance_raisons.py <fichier JSON de sortie> [répliques]

Pour chaque configuration (les vrais taux d'action désalignée des six bras sous les deux cadrages, le nombre de graines,
de scénarios et de générations, la variabilité entre entraînements), on simule des comptes, on applique la porte telle
que porte_des_raisons.py la lit (les mêmes comparaisons, le même bootstrap croisé, Student sous huit graines, la même
table), et l'on compte la part de chaque issue.

Le modèle des comptes :
- la difficulté d'un scénario est commune à tous les bras (écart-type scen_sd, en taux) ;
- un entraînement (un bras, une graine) a son propre écart (seed_sd, en taux) : les graines sont partagées entre bras,
  mais chaque bras s'entraîne à part ;
- chaque génération est un tirage de Bernoulli au taux qui en résulte.
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import porte_des_raisons as pr  # noqa: E402

PAIRS = (("reasons", "actions_only"), ("reasons", "neutral_text"), ("reasons", "other_reasoning"),
         ("neutral_text", "actions_only"), ("other_reasoning", "neutral_text"), ("other_reasoning", "generic_principles"),
         ("reflection", "reasons"), ("reflection", "actions_only"))


def simulate_counts(rng, rates, seeds, scenarios, gens, scen_sd=0.05, seed_sd=0.0):
    """Les comptes [graine, scénario, bras] d'action désalignée, et les épisodes, aux taux donnés par bras."""
    diff = rng.normal(0, scen_sd, scenarios)
    p = np.empty((seeds, scenarios, len(pr.ARMS)))
    for a, arm in enumerate(pr.ARMS):
        run = rng.normal(0, seed_sd, seeds)
        p[:, :, a] = rates[arm] + diff[None, :] + run[:, None]
    n = np.full(p.shape, float(gens))
    k = rng.binomial(gens, np.clip(p, 0.005, 0.995)).astype(float)
    return k, n


def comparisons_from(k, n, margin=3.0, n_boot=200, seed=0):
    """Les comparaisons de porte_des_raisons.comparisons, sur des comptes déjà faits."""
    reps = pr.bootstrap_rates(k, n, n_boot, seed)
    ix = {a: i for i, a in enumerate(pr.ARMS)}
    return {f"{x}-{y}": pr.compare(k, n, reps, ix[x], ix[y], margin) for x, y in PAIRS}


def outcome(rng, cfg, margin=3.0, minimal_effect=5.0, n_boot=200, seed=0):
    """L'issue de la table A.2 sur une réplique (sans la lecture à trois issues : aucune issue invalide n'est simulée)."""
    shared = {key: cfg[key] for key in ("seeds", "scenarios", "gens", "scen_sd", "seed_sd") if key in cfg}
    kd, nd = simulate_counts(rng, cfg["deploiement"], **shared)
    ke, ne = simulate_counts(rng, cfg.get("evaluation", cfg["deploiement"]), **shared)
    dep = comparisons_from(kd, nd, margin, n_boot, seed)
    ev = comparisons_from(ke, ne, margin, n_boot, seed + 1)
    return pr.issue_of(dep, ev, minimal_effect)


def power(cfg, reps=100, n_boot=200, seed=0):
    """La part de chaque issue sur reps répliques."""
    rng = np.random.default_rng(seed)
    counts = {}
    for r in range(reps):
        issue = outcome(rng, cfg, n_boot=n_boot, seed=r)
        counts[issue] = counts.get(issue, 0) + 1
    return {k: round(v / reps, 3) for k, v in sorted(counts.items(), key=lambda kv: -kv[1])}


def arms(a, n, o, g, r, f):
    return {"actions_only": a, "neutral_text": n, "other_reasoning": o, "generic_principles": g, "reasons": r, "reflection": f}


# Les vrais états simulés, à la distance lointaine, sous cadrage de déploiement (taux d'action désalignée) :
TRUTHS = {
    # le gain des raisons, avec un gain de lien : 10 points sur les actions seules, 6 sur le texte neutre, 3 sur
    # l'autre situation
    "lien": arms(0.30, 0.26, 0.23, 0.23, 0.20, 0.20),
    # le gain de format : le texte neutre fait autant que les raisons, 10 points sous les actions seules
    "format": arms(0.30, 0.20, 0.20, 0.20, 0.20, 0.20),
    # aucun gain, sous les deux cadrages
    "aucun": arms(0.30, 0.30, 0.30, 0.30, 0.30, 0.30),
    # un gain de 3 points seulement, sous l'effet minimal
    "petit": arms(0.30, 0.29, 0.28, 0.28, 0.27, 0.27),
}
EXPECTED = {"lien": "gain des raisons, avec un gain de lien", "format": "gain de format", "aucun": "pas de gain",
            "petit": "un gain plus petit que l'effet minimal"}

GRID = []
for truth in TRUTHS:
    for seeds in (2, 3, 5):
        for scenarios, gens in ((200, 5), (400, 5), (400, 10)):
            for seed_sd in (0.0, 0.02):
                GRID.append({"truth": truth, "deploiement": TRUTHS[truth], "seeds": seeds, "scenarios": scenarios,
                             "gens": gens, "scen_sd": 0.05, "seed_sd": seed_sd})


def main(dest, reps=100):
    rows = []
    for cfg in GRID:
        p = power(cfg, reps=reps)
        row = {k: v for k, v in cfg.items() if k != "deploiement"}
        row["issues"] = p
        row["right"] = p.get(EXPECTED[cfg["truth"]], 0.0)
        rows.append(row)
        print(row, flush=True)
    Path(dest).write_text(json.dumps({"reps": reps, "expected": EXPECTED, "truths": TRUTHS, "rows": rows},
                                     ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 100)
