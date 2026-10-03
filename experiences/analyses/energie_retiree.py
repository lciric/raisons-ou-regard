"""L'énergie que retire l'inhibition de « je suis évalué », contre des sous-espaces aléatoires de même rang (sans GPU).

    python analyses/energie_retiree.py <dossier out du run d'extraction> <fichier JSON de sortie>

La contre-lecture vierge de la v1.4 (point bloquant sur l'appariement, question 5 aux auteurs) demande quelle énergie
l'inhibition retire, comparée à des sous-espaces aléatoires de même rang : un sous-espace tiré uniformément en dimension
4 096 retire de l'ordre de k/4 096 de l'énergie, une direction issue d'une décomposition des différences
d'activations, beaucoup plus. Elle propose d'apparier sur l'énergie retirée et de tirer les aléatoires selon la
covariance des activations.

Ce que le script mesure, couche par couche et aux rangs 1 à 32, sur les activations gardées par le job d'extraction (le
dernier jeton des prompts, après l'en-tête de l'assistant) :
- la part de l'énergie centrée des prompts du jeu de validation (tenus à part de l'extraction) que retire la projection
  entière sur le sous-espace de « je suis évalué » ;
- la même part pour 20 sous-espaces tirés uniformément ;
- la même part pour 20 sous-espaces tirés selon la covariance des activations du jeu d'extraction (des combinaisons
  aléatoires des activations centrées), orthogonalisés contre le sous-espace de « je suis évalué » au rang 32, puis
  orthonormalisés.
Puis, aux rangs 1, 8 et 32, le plus petit rang (multiple du rang de l'inhibition, jusqu'à 8 fois) auquel 10 tirages
sur 10 selon la covariance retirent au moins l'énergie de l'inhibition : le rang qu'il faut laisser libre pour apparier
sur l'énergie.
Les activations ne sont que celles du dernier jeton de prompts d'indices : l'inhibition, elle, porte sur toutes les
positions. C'est une indication de l'ordre de grandeur, pas la mesure sur les réponses.
"""
import json
import sys

import torch
from safetensors.torch import load_file

RANKS = (1, 2, 4, 8, 16, 32)


def share(Hc, Q, total):
    return float(((Hc @ Q) ** 2).sum(1).mean() / total)


def main(out_dir, dest, seed=1, n_random=20):
    st = {k: v.double() for k, v in load_file(f"{out_dir}/states.safetensors").items()}
    sub = load_file(f"{out_dir}/eval_subspace.safetensors")
    val = torch.cat([st["validation.eval"], st["validation.deploy"]])
    ext = torch.cat([st["extraction.eval"], st["extraction.deploy"]])
    g = torch.Generator().manual_seed(seed)
    n_layers, width = val.shape[1], val.shape[2]
    res = {"seed": seed, "n_random": n_random, "prompts": int(val.shape[0]), "layers": {}}
    for layer in range(1, n_layers + 1):
        H = val[:, layer - 1]
        Hc = H - H.mean(0, keepdim=True)
        total = (Hc ** 2).sum(1).mean()
        E = ext[:, layer - 1]
        Ec = E - E.mean(0, keepdim=True)
        B = sub[f"layer_{layer:02d}.basis"].double()
        Ec_out = Ec - (Ec @ B.T) @ B                      # the covariance draws never contain the target subspace
        row = {}
        for k in RANKS:
            uni, cov = [], []
            for _ in range(n_random):
                Q, _ = torch.linalg.qr(torch.randn(width, k, generator=g, dtype=torch.float64))
                uni.append(share(Hc, Q, total))
                Qc, _ = torch.linalg.qr(Ec_out.T @ torch.randn(Ec_out.shape[0], k, generator=g, dtype=torch.float64))
                cov.append(share(Hc, Qc, total))
            uni, cov = torch.tensor(uni), torch.tensor(cov)
            inh = share(Hc, B[:k].T, total)
            row[str(k)] = {"inhibition": round(inh, 5),
                           "uniform": {"median": round(float(uni.median()), 6), "max": round(float(uni.max()), 6)},
                           "covariance": {"median": round(float(cov.median()), 5), "min": round(float(cov.min()), 5),
                                          "max": round(float(cov.max()), 5)},
                           "inhibition_over_uniform_median": round(inh / float(uni.median()), 1),
                           "covariance_reaches_inhibition": int((cov >= inh).sum())}
        free = {}
        for k in (1, 8, 32):
            inh = share(Hc, B[:k].T, total)
            free[str(k)] = None
            for m in (1, 2, 3, 4, 6, 8):
                ok = 0
                for _ in range(10):
                    Qc, _ = torch.linalg.qr(Ec_out.T @ torch.randn(Ec_out.shape[0], k * m, generator=g, dtype=torch.float64))
                    ok += share(Hc, Qc, total) >= inh
                if ok == 10:
                    free[str(k)] = k * m
                    break
        row["covariance_rank_to_match"] = free
        res["layers"][str(layer)] = row
    with open(dest, "w", encoding="utf8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    return res


if __name__ == "__main__":
    r = main(sys.argv[1], sys.argv[2])
    for layer in ("6", "19", "21", "23", "32"):
        for k in ("1", "8", "32"):
            v = r["layers"][layer][k]
            need = r["layers"][layer]["covariance_rank_to_match"][k]
            print(f"couche {layer:>2} rang {k:>2} : inhibition {v['inhibition']:.4f} ; uniformes {v['uniform']['median']:.5f} "
                  f"({v['inhibition_over_uniform_median']:.0f} fois moins) ; covariance {v['covariance']['median']:.4f}, "
                  f"{v['covariance_reaches_inhibition']}/20 atteignent l'inhibition ; au rang {need}, 10 sur 10")
