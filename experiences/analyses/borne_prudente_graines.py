"""La borne prudente de la variance du pilote, qui fixera le nombre de graines par bras au second temps. Exploratoire,
sans données réelles : la suite de pilote_variance.py.

    python analyses/borne_prudente_graines.py <fichier JSON de sortie> [répliques]

**Pourquoi** (9 octobre 2026, 9 h 45 UTC, écrit avant le calcul). La décision 53 garde deux graines par bras au pilote,
et demande une règle écrite avant lui : la simulation du second temps lira une borne prudente de la variance des
contrastes par graine, et non son estimation seule. Avec 6 bras et 2 graines, l'analyse de variance bras × graine n'a
que 5 degrés de liberté ; l'estimation se trompe du simple au double et tombe souvent à zéro (pilote_variance.py).

**Les règles comparées.** Chacune donne une variance des contrastes par graine, v = 2σ²(1 − ρ), d'où un nombre de
graines n(v) :
- l'estimation seule (la variance propre de l'analyse de variance, le bruit binomial retiré, ramenée à 0 si négative) ;
- la borne haute unilatérale à 80 %, puis à 90 %, de la loi du khi-deux à 5 degrés de liberté, appliquée au carré
  moyen résiduel avant le retrait du bruit binomial ;
- l'estimation seule, avec un plancher fixé d'avance à l'écart de 2 points entre entraînements (ρ = 0).

**Le nombre de graines n(v)** vient des simulations de puissance du 9 octobre : 8 graines suffisent à 1 point d'écart,
de 10 à 16 à 2 points, et 16 ne suffisent pas à 3 points. On l'approche par n(v) = ⌈6,3 + 0,83 v⌉ (v en points au
carré), entre 5 et 64 : 8 graines à v = 2, 13 à v = 8, 21 à v = 18. C'est une approximation déclarée, pour comparer les
règles entre elles, pas pour fixer le nombre.

**Ce qu'on mesure**, pour chaque vérité (σ de 1, 2 ou 3 points ; ρ de 0, 0,5 ou 0,8) :
- la part des pilotes où la règle donne au moins le nombre de graines qu'il faut vraiment, n(v vrai) ;
- le nombre médian de graines qu'elle donne, et son 90ᵉ centile (le coût).

**Ce que j'attends** : l'estimation seule ne suffit que dans la moitié des pilotes environ, souvent moins quand ρ est
grand ; la borne à 80 % suffit dans environ 80 % des pilotes, pour un coût de l'ordre du double ; le plancher protège à
ρ = 0 et coûte trop quand ρ est grand.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pilote_variance import ARMS, GENS, SCENARIOS, pilot_rates  # noqa: E402

CHI2_LOW_5DF = {0.80: 2.3425, 0.90: 1.6103}      # quantiles inférieurs à 20 % et à 10 % du khi-deux à 5 degrés


def n_seeds(v):
    """Le nombre de graines approché pour une variance des contrastes par graine v (en points au carré)."""
    return int(min(max(math.ceil(6.3 + 0.83 * v), 5), 64))


def residual_ms(rates):
    """Le carré moyen résiduel de l'analyse de variance bras × graine, et le bruit binomial d'un taux (en points²)."""
    S, A = rates.shape
    resid = rates - rates.mean(axis=0, keepdims=True) - rates.mean(axis=1, keepdims=True) + rates.mean()
    ms = (resid ** 2).sum() / ((S - 1) * (A - 1))
    binom = float(np.mean(rates * (1 - rates))) / (SCENARIOS * GENS)
    return 1e4 * ms, 1e4 * binom


def rules(rates):
    """La variance des contrastes par graine (points²) selon chaque règle."""
    ms, binom = residual_ms(rates)
    df = (rates.shape[0] - 1) * (rates.shape[1] - 1)
    out = {"estimation": 2 * max(ms - binom, 0.0)}
    for level, q in CHI2_LOW_5DF.items():
        out[f"borne_{int(level * 100)}"] = 2 * max(df * ms / q - binom, 0.0)
    out["plancher_2_points"] = max(out["estimation"], 2 * 2.0 ** 2)
    return out


def main(dest, reps=2000):
    assert ARMS == 6
    rng = np.random.default_rng(20261009)
    rows = []
    for sigma in (0.01, 0.02, 0.03):
        for rho in (0.0, 0.5, 0.8):
            v_true = 2 * (100 * sigma) ** 2 * (1 - rho)
            need = n_seeds(v_true)
            got = {}
            for _ in range(reps):
                for name, v in rules(pilot_rates(rng, 2, sigma, rho)).items():
                    got.setdefault(name, []).append(n_seeds(v))
            row = {"sigma_points": 100 * sigma, "rho": rho, "v_true": round(v_true, 2), "seeds_needed": need, "rules": {}}
            for name, ns in got.items():
                ns = np.array(ns)
                row["rules"][name] = {"share_enough": round(float(np.mean(ns >= need)), 3),
                                      "median_seeds": int(np.median(ns)), "p90_seeds": int(np.percentile(ns, 90))}
            rows.append(row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
    Path(dest).write_text(json.dumps({"reps": reps, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
