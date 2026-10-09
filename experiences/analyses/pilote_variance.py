"""Ce que le pilote peut estimer de la variance qui fixe le nombre de graines. Exploratoire, sans données réelles.

    python analyses/pilote_variance.py <fichier JSON de sortie> [répliques]

**Pourquoi** (9 octobre 2026, 2 h 20 UTC, écrit avant le calcul). La simulation de puissance dit que le nombre de
graines par bras dépend de la variance des contrastes par graine entre bras : 2σ²(1 − ρ), σ l'écart d'un entraînement,
ρ sa corrélation entre bras au sein d'une graine (8 graines si ρ = 0,8 à σ = 2 points, de 12 à 16 si ρ = 0). Le texte
déposé prévoit deux graines par bras au pilote (section 2.3), et la simulation de l'amendement du second temps reprend la
variance du pilote (section 3.5).

**La question** : avec 2, 3 ou 4 graines par bras et six bras, de combien l'estimation de l'écart des contrastes,
√(2σ²(1 − ρ)), s'écarte-t-elle de sa vraie valeur ? On rapporte l'intervalle qui contient 90 % des estimations, en
rapport à la vraie valeur.

**L'estimateur** : les taux de chaque entraînement (un bras, une graine), leur bruit binomial retiré ; une analyse de
variance bras × graine, sans interaction, sépare la part commune à la graine (ρσ²) et la part propre à l'entraînement
((1 − ρ)σ²) ; l'écart des contrastes est √(2 × la part propre). Les moments négatifs sont ramenés à 0.

**Ce que j'attends** : à deux graines, la part propre a 5 degrés de liberté (6 bras × 1 graine de plus, moins 1) et
l'estimation varie à peu près du simple au triple ; à quatre graines, elle se resserre nettement.
"""
import json
import sys
from pathlib import Path

import numpy as np

SCENARIOS, GENS, ARMS = 400, 5, 6


def pilot_rates(rng, seeds, sigma, rho, base=0.30, scen_sd=0.05):
    """Les taux [graine, bras] d'un pilote : une difficulté par scénario, l'écart de chaque entraînement (une part
    commune à la graine et une part propre), des générations de Bernoulli."""
    diff = rng.normal(0, scen_sd, SCENARIOS)
    common = rng.normal(0, sigma, seeds)
    rates = np.empty((seeds, ARMS))
    for a in range(ARMS):
        run = np.sqrt(rho) * common + np.sqrt(1 - rho) * rng.normal(0, sigma, seeds)
        p = np.clip(base + diff[None, :] + run[:, None], 0.005, 0.995)
        rates[:, a] = rng.binomial(GENS, p).sum(axis=1) / (SCENARIOS * GENS)
    return rates


def estimate_contrast_sd(rates):
    """L'écart des contrastes par graine entre bras, √(2 × la part propre), par l'analyse de variance bras × graine
    sans interaction, le bruit binomial retiré."""
    S, A = rates.shape
    grand = rates.mean()
    resid = rates - rates.mean(axis=0, keepdims=True) - rates.mean(axis=1, keepdims=True) + grand
    ms_resid = (resid ** 2).sum() / ((S - 1) * (A - 1))
    binom = float(np.mean(rates * (1 - rates))) / (SCENARIOS * GENS)       # la variance binomiale d'un taux
    own = max(ms_resid - binom, 0.0)
    return float(np.sqrt(2 * own))


def main(dest, reps=2000):
    rng = np.random.default_rng(20261009)
    rows = []
    for sigma in (0.01, 0.02):
        for rho in (0.0, 0.5, 0.8):
            truth = np.sqrt(2 * sigma ** 2 * (1 - rho))
            for seeds in (2, 3, 4):
                est = np.array([estimate_contrast_sd(pilot_rates(rng, seeds, sigma, rho)) for _ in range(reps)])
                ratio = est / truth
                row = {"sigma_points": 100 * sigma, "rho": rho, "seeds": seeds, "true_contrast_sd_points": round(100 * truth, 3),
                       "ratio_p05": round(float(np.percentile(ratio, 5)), 3), "ratio_median": round(float(np.median(ratio)), 3),
                       "ratio_p95": round(float(np.percentile(ratio, 95)), 3), "share_zero": round(float(np.mean(est == 0)), 3)}
                rows.append(row)
                print(json.dumps(row, ensure_ascii=False), flush=True)
    Path(dest).write_text(json.dumps({"reps": reps, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
