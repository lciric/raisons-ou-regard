"""Combien de graines par bras la porte des raisons demande-t-elle, selon l'écart entre entraînements ? Exploratoire,
sans données réelles : la suite de puissance_raisons.py (même modèle des comptes, même porte, mêmes vérités), au-delà de
cinq graines.

    python analyses/puissance_raisons_graines.py <fichier JSON de sortie> [répliques]

À partir de huit graines, la porte ne prend plus l'intervalle de Student (section 5.3) : le bootstrap croisé décide seul.
"""
import json
import sys
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from puissance_raisons import EXPECTED, TRUTHS, power  # noqa: E402

GRID = []
for truth in TRUTHS:
    for seeds in (5, 8, 10, 12, 16):
        for seed_sd in (0.01, 0.02, 0.03):
            GRID.append({"truth": truth, "deploiement": TRUTHS[truth], "seeds": seeds, "scenarios": 400, "gens": 5,
                         "scen_sd": 0.05, "seed_sd": seed_sd})


def row_of(args):
    """Une configuration ; chacune tire ses répliques de sa propre graine, l'ordre des calculs ne change rien."""
    cfg, reps = args
    p = power(cfg, reps=reps)
    row = {k: v for k, v in cfg.items() if k != "deploiement"}
    row["issues"] = p
    row["right"] = p.get(EXPECTED[cfg["truth"]], 0.0)
    print(json.dumps({k: row[k] for k in ("truth", "seeds", "seed_sd", "right")}, ensure_ascii=False), flush=True)
    return row


def main(dest, reps=200, workers=4):
    with Pool(workers) as pool:
        rows = pool.map(row_of, [(cfg, reps) for cfg in GRID])
    Path(dest).write_text(json.dumps({"reps": reps, "expected": EXPECTED, "truths": TRUTHS, "rows": rows},
                                     ensure_ascii=False, indent=1), encoding="utf8")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 200)
