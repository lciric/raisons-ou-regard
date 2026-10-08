"""Les cas simulés de l'audit du 8 octobre 2026 (claude/AUDIT_REGLES_DEPOSEES_2026-10-08.md), là où le texte déposé
disait autre chose que le code, ou ne tranchait pas. Aucune donnée réelle.

    python analyses/cas_audit_2026-10-08.py

Les fichiers déposés (commit 9c46aad et avant) rendaient : « un gain plus petit que l'effet minimal » ; la ligne [1] ;
la ligne [5]. Depuis leur correction (décision 46), les mêmes cas rendent : « non conclusif » ; la ligne [6] ; les
lignes [4, 5]. Les tests (tests/test_porte_des_raisons.py, tests/test_regle_du_regard.py) gardent ces cas.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import porte_des_raisons as pr  # noqa: E402
import regle_du_regard as rr  # noqa: E402


def gate_episodes(rates, seeds=8, scenarios=200, generations=5, seed=0):
    """Des épisodes sans intervention, aux taux d'action désalignée donnés par bras, sous les deux cadrages."""
    rng = np.random.default_rng(seed)
    out = []
    for arm, p in rates.items():
        for s in range(seeds):
            for c in range(scenarios):
                for _ in range(generations):
                    for framing in ("deploiement", "evaluation"):
                        out.append({"arm": arm, "seed": s, "scenario": f"s{c}", "framing": framing, "slot": "libre",
                                    "family": "f", "intervention": "none",
                                    "outcome": "desaligne" if rng.random() < p else "aligne"})
    return out


def gaze_episodes(rates, seeds=8, scenarios=200, generations=5, seed=0):
    """Des épisodes des actions seules et des raisons, sous l'inhibition et le comparateur, cadrage de déploiement."""
    rng = np.random.default_rng(seed)
    out = []
    for (arm, iv), p in rates.items():
        for s in range(seeds):
            for c in range(scenarios):
                for _ in range(generations):
                    out.append({"arm": arm, "seed": s, "scenario": f"s{c}", "framing": "deploiement", "slot": "libre",
                                "family": "f", "intervention": iv,
                                "outcome": "desaligne" if rng.random() < p else "aligne"})
    return out


def cas_porte():
    """Les raisons font mieux que les actions seules d'au moins l'effet minimal, et mieux que le texte neutre ; mais le
    raisonnement d'une autre situation fait mieux que les raisons. La table A.2 n'a pas de ligne pour ce cas."""
    eps = gate_episodes({"actions_only": 0.40, "neutral_text": 0.30, "other_reasoning": 0.10,
                         "generic_principles": 0.20, "reasons": 0.20, "reflection": 0.20})
    return pr.gate(eps, n_boot=300)


def cas_fieller_non_borne():
    """Sous le comparateur, aucun avantage ; sous l'inhibition, les raisons font pire que les actions seules."""
    A, R, I, K = rr.ACTIONS, rr.RAISONS, rr.INHIBITION, rr.COMPARATEUR
    return rr.decide(gaze_episodes({(A, K): 0.30, (R, K): 0.30, (A, I): 0.30, (R, I): 0.45}), n_boot=400)


def cas_evalue_inactif():
    """Un avantage qui survit tel quel (f proche de 0), « évalué » n'étant pas actif sous déploiement."""
    A, R, I, K = rr.ACTIONS, rr.RAISONS, rr.INHIBITION, rr.COMPARATEUR
    eps = gaze_episodes({(A, K): 0.40, (R, K): 0.20, (A, I): 0.40, (R, I): 0.20}, scenarios=400, generations=10)
    return rr.decide(eps, conditions={"evalue_actif": False}, n_boot=400)


if __name__ == "__main__":
    g = cas_porte()
    for k in ("reasons-actions_only", "reasons-neutral_text", "reasons-other_reasoning"):
        d = g["deploiement"][k]
        print(f"porte : {k} {d['diff']:.2f} points, IC à 95 % ({d['ci95'][0]:.2f} ; {d['ci95'][1]:.2f}), classe {d['class']}")
    print("porte : issue du code :", g["issue"])
    d4 = cas_fieller_non_borne()
    print(f"regard, Fieller non borné : D {d4['D']:.2f}, IC à 95 % ({d4['ci95_D'][0]:.2f} ; {d4['ci95_D'][1]:.2f}), "
          f"avantage sous le comparateur {d4['advantage_comparator']:.2f}, Fieller à 90 % {d4['fieller90']}, lignes {d4['lines']}")
    d5 = cas_evalue_inactif()
    f5 = d5["fieller90"]
    print(f"regard, « évalué » inactif : Fieller à 90 % ({f5[0]:.3f} ; {f5[1]:.3f}), lignes {d5['lines']}")
