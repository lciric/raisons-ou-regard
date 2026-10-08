"""Le choix des couches et la condition lexicale de l'instrument, par la règle du texte déposé (annexe C.2, « Layer
choice » ; annexe A.1, troisième condition de la porte), lus sans machine sur les états qu'une extraction a enregistrés.

La règle déposée : « On one half of the validation set: the window of five consecutive layers with the best mean probe
AUROC, among layers where the probe beats the bag of words (a margin of 0). The other half gives the reported value. »
Et la porte échoue si « a bag of words separates the validation set at least as well as the probe ».

Les choix d'exécution, écrits et commités avant la première lecture (8 octobre 2026, la nuit ; décision 47) :
- **les paires de l'ajustement** : les 150 premières paires d'extraction, rangées par identifiant (annexe C.2 : « from
  7 October 2026, every subspace is extracted on extraction pairs 0–149 only ») ;
- **la sonde** : la régression logistique du job d'extraction (`extract_eval.logistic_probe`), apprise couche par couche
  sur les états de ces paires (leurs deux contextes, les deux côtés), lue sur la validation ;
- **le sac de mots** : le Bayes naïf de `rrdata.lexical`, appris sur les indices de ces mêmes paires (chaque indice une
  fois), lu sur les indices de la validation, un par invite, alignés sur les états ;
- **les deux moitiés de la validation** : ses paires rangées par identifiant, une sur deux (A : les rangs pairs, où l'on
  choisit ; B : les rangs impairs, où l'on rapporte) ;
- **une fenêtre** n'entre que si chacune de ses cinq couches bat le sac de mots sur la moitié A ;
- **la condition lexicale** se lit sur la moitié B : la sonde, en moyenne sur la fenêtre choisie, fait mieux que le sac
  de mots ;
- **les couches** sont numérotées de 1 à 32 (l'état après chaque couche du décodeur), comme les sous-espaces.

    python analyses/choix_des_couches.py <states.safetensors> <states.json> <dossier des indices> <sortie.json>
"""
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "donnees"))

PREMIERES_PAIRES = 150
FENETRE = 5


def cue_texts(path):
    """{(paire, polarité): texte de l'indice}."""
    out = {}
    with open(path, encoding="utf8") as fh:
        for line in fh:
            if line.strip():
                r = json.loads(line)
                out[(r["pair"], r["polarity"])] = r["text"]
    return out


def halves(pair_ids):
    """Les paires de la validation, rangées par identifiant, une sur deux : (A, B)."""
    u = sorted(set(pair_ids))
    return set(u[0::2]), set(u[1::2])


def windows(beats, values, width=FENETRE):
    """Les fenêtres de width couches consécutives dont chaque couche bat le sac de mots, avec leur valeur moyenne :
    [(moyenne, première couche, indices)]."""
    out = []
    for s in range(len(values) - width + 1):
        if all(beats[s:s + width]):
            out.append((statistics.fmean(values[s:s + width]), s, list(range(s, s + width))))
    return out


def lire(states, index, cues_dir, first_pairs=PREMIERES_PAIRES, width=FENETRE, margin=0.0):
    """La lecture de la règle. states : {"extraction.eval": [n, couches, largeur], ...} ; index : le states.json."""
    import torch  # noqa: WPS433
    from rrdata.lexical import NaiveBayes, auroc as lex_auroc  # noqa: WPS433
    from rrexp.jobs.extract_eval import auroc, logistic_probe  # noqa: WPS433

    ext_pairs, val_pairs = index["extraction"]["pairs"], index["validation"]["pairs"]
    kept = set(sorted(set(ext_pairs))[:first_pairs])
    rows = [i for i, p in enumerate(ext_pairs) if p in kept]
    half_a, half_b = halves(val_pairs)
    rows_a = [i for i, p in enumerate(val_pairs) if p in half_a]
    rows_b = [i for i, p in enumerate(val_pairs) if p in half_b]

    t_ext, t_val = cue_texts(Path(cues_dir) / "extraction.jsonl"), cue_texts(Path(cues_dir) / "validation.jsonl")
    ev_u = sorted({t_ext[(p, "eval")] for p in kept})
    de_u = sorted({t_ext[(p, "deploy")] for p in kept})
    nb = NaiveBayes().fit(ev_u + de_u, [1] * len(ev_u) + [0] * len(de_u))

    def lexical(rws):
        e = [t_val[(val_pairs[i], "eval")] for i in rws]
        d = [t_val[(val_pairs[i], "deploy")] for i in rws]
        return lex_auroc([nb.score(t) for t in e + d], [1] * len(e) + [0] * len(d))

    lex_a, lex_b = lexical(rows_a), lexical(rows_b)
    n_layers = states["extraction.eval"].shape[1]
    per_layer = []
    for l in range(n_layers):
        x = torch.cat([states["extraction.eval"][rows, l], states["extraction.deploy"][rows, l]]).float()
        score = logistic_probe(x, [1] * len(rows) + [0] * len(rows))

        def read(rws, l=l, score=score):
            z = torch.cat([states["validation.eval"][rws, l], states["validation.deploy"][rws, l]]).float()
            return float(auroc(score(z), [1] * len(rws) + [0] * len(rws)))
        per_layer.append({"layer": l + 1, "probe_a": round(read(rows_a), 4), "probe_b": round(read(rows_b), 4)})
    beats = [m["probe_a"] > lex_a + margin for m in per_layer]
    wins = windows(beats, [m["probe_a"] for m in per_layer], width)
    out = {"extraction_pairs": len(kept), "validation_pairs": {"a": len(half_a), "b": len(half_b)},
           "lexical": {"a": round(lex_a, 4), "b": round(lex_b, 4)}, "margin": margin, "per_layer": per_layer,
           "layers_beating_the_bag_of_words_a": [m["layer"] for m, b in zip(per_layer, beats) if b]}
    if not wins:
        out.update({"window": None, "lexical_condition": False,
                    "verdict": "aucune fenêtre de cinq couches ne bat le sac de mots sur la moitié A : la condition lexicale échoue"})
        return out
    mean_a, start, idx = max(wins)
    probe_b = statistics.fmean(per_layer[i]["probe_b"] for i in idx)
    passes = probe_b > lex_b + margin
    out.update({"window": [per_layer[i]["layer"] for i in idx], "probe_a_mean": round(mean_a, 4),
                "probe_b_mean": round(probe_b, 4), "lexical_condition": passes,
                "verdict": ("la condition lexicale tient : sur la moitié B, la sonde fait mieux que le sac de mots"
                            if passes else "la condition lexicale échoue : sur la moitié B, le sac de mots fait aussi bien que la sonde")})
    return out


if __name__ == "__main__":
    from safetensors.torch import load_file
    states = load_file(sys.argv[1])
    index = json.loads(Path(sys.argv[2]).read_text(encoding="utf8"))
    res = lire(states, index, sys.argv[3])
    Path(sys.argv[4]).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf8")
    print(json.dumps({k: v for k, v in res.items() if k != "per_layer"}, ensure_ascii=False, indent=1))
