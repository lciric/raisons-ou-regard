"""Les contrôles de l'extraction de « je suis évalué » qui se calculent sans GPU, sur les activations gardées par le job.

    python analyses/controles_extraction.py <dossier out du run> <dossier des jeux d'indices> <fichier JSON de sortie>

Le dossier out tient states.safetensors, states.json et eval_subspace.safetensors (dépôt de résultats,
runs/<run_id>/out/). Il faut torch et safetensors (les paquets des machines).

1. L'accord apparié (la part des paires dont le prompt d'évaluation se projette plus haut que son jumeau de
   déploiement), avec ses deux nuls : des directions aléatoires, et la différence moyenne de l'extraction à polarités
   équilibrées. Le 95e centile de max(p, 1 - p), puisqu'une direction nulle n'a pas d'orientation.
2. La ligne de base lexicale : un sac de mots, appris sur les textes des indices d'extraction, lu sur les textes des
   autres jeux ; et une liste de mots d'évaluation, écrite après lecture des indices (une indication, pas un test).
3. La validation restreinte aux paires dont l'indice d'évaluation ne contient aucun mot de cette liste : la direction,
   la sonde et l'accord apparié, et le sac de mots sur les mêmes paires.
"""
import json
import re
import sys
from pathlib import Path

import torch
from safetensors.torch import load_file

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rrexp.jobs.extract_eval import auroc, logistic_probe  # noqa: E402

KEYWORDS = re.compile(r"eval|test|bench|rubric|scor|grad(er|ing)|assess|judge|rater|annotat", re.I)


def words(text):
    return re.findall(r"[a-z]+", text.lower())


def read_jsonl(path):
    with open(path, encoding="utf8") as fh:
        return [json.loads(l) for l in fh if l.strip()]


def p95_unoriented(values):
    v = torch.as_tensor(values, dtype=torch.float64)
    return round(float(torch.quantile(torch.maximum(v, 1 - v), 0.95)), 4)


def main(out_dir, cue_dir, dest, seed=1, n_random=200, n_flips=50):
    out_dir, cue_dir = Path(out_dir), Path(cue_dir)
    st = {k: v.float() for k, v in load_file(str(out_dir / "states.safetensors")).items()}
    sub = load_file(str(out_dir / "eval_subspace.safetensors"))
    meta = json.loads((out_dir / "states.json").read_text(encoding="utf8"))
    g = torch.Generator().manual_seed(seed)
    n_layers, width = st["validation.eval"].shape[1], st["validation.eval"].shape[2]
    rand = torch.randn(n_random, width, generator=g)
    rand = rand / rand.norm(dim=1, keepdim=True)
    dex = st["extraction.eval"] - st["extraction.deploy"]
    n = dex.shape[0]
    res = {"seed": seed, "n_random": n_random, "n_flips": n_flips, "paired": {}, "lexical": {}, "validation_without_keywords": {}}

    # 1. paired agreement and its nulls
    for key in ("validation", "fresh_probe"):
        ev, de = st[f"{key}.eval"], st[f"{key}.deploy"]
        rows = []
        for l in range(n_layers):
            d0 = sub[f"layer_{l + 1:02d}.basis"][0]
            pr = ((ev[:, l] @ rand.T) > (de[:, l] @ rand.T)).double().mean(0)
            nulls = []
            for _ in range(n_flips):
                f = torch.ones(n)
                f[torch.randperm(n, generator=g)[: n // 2]] = -1.0
                mu = (dex[:, l] * f[:, None]).mean(0)
                mu = mu / mu.norm()
                nulls.append(float((ev[:, l] @ mu > de[:, l] @ mu).double().mean()))
            rows.append({"layer": l + 1, "paired": round(float((ev[:, l] @ d0 > de[:, l] @ d0).double().mean()), 4),
                         "random_p95": p95_unoriented(pr), "pipeline_null_p95": p95_unoriented(nulls)})
        res["paired"][key] = rows

    # 2. lexical baselines
    train = read_jsonl(cue_dir / "extraction.jsonl")
    vocab = sorted({w for r in train for w in words(r["text"])})
    index = {w: i for i, w in enumerate(vocab)}

    def bow(rs):
        x = torch.zeros(len(rs), len(vocab))
        for i, r in enumerate(rs):
            for w in words(r["text"]):
                if w in index:
                    x[i, index[w]] = 1.0
        return x

    lex = logistic_probe(bow(train), [int(r["polarity"] == "eval") for r in train], l2=1e-1)
    for key in ("validation", "fresh_probe"):
        rs = read_jsonl(cue_dir / f"{key}.jsonl")
        y = [int(r["polarity"] == "eval") for r in rs]
        res["lexical"][key] = {"bag_of_words_from_extraction": round(auroc(lex(bow(rs)), y), 4),
                               "keyword_list": round(auroc([float(bool(KEYWORDS.search(r["text"]))) for r in rs], y), 4),
                               "eval_cues_with_keyword": sum(bool(KEYWORDS.search(r["text"])) for r in rs if r["polarity"] == "eval"),
                               "eval_cues": sum(r["polarity"] == "eval" for r in rs)}
    res["lexical"]["vocabulary"] = len(vocab)

    # 3. validation without the keywords
    cues = {}
    for r in read_jsonl(cue_dir / "validation.jsonl"):
        cues.setdefault(r["pair"], {})[r["polarity"]] = r
    keep_pairs = sorted(p for p in cues if not KEYWORDS.search(cues[p]["eval"]["text"]))
    rows_idx = [i for i, pid in enumerate(meta["validation"]["pairs"]) if pid in set(keep_pairs)]
    rs = [cues[p][s] for p in keep_pairs for s in ("eval", "deploy")]
    ev, de = st["validation.eval"][rows_idx], st["validation.deploy"][rows_idx]
    xe, xd = st["extraction.eval"], st["extraction.deploy"]
    y = [1] * len(rows_idx) + [0] * len(rows_idx)
    layers = []
    for l in range(n_layers):
        d0 = sub[f"layer_{l + 1:02d}.basis"][0]
        probe = logistic_probe(torch.cat([xe[:, l], xd[:, l]]), [1] * len(xe) + [0] * len(xd))
        x = torch.cat([ev[:, l], de[:, l]])
        layers.append({"layer": l + 1, "direction": round(auroc(x @ d0, y), 4), "probe": round(auroc(probe(x), y), 4),
                       "paired": round(float((ev[:, l] @ d0 > de[:, l] @ d0).double().mean()), 4)})
    res["validation_without_keywords"] = {
        "pairs": len(keep_pairs), "prompts_per_side": len(rows_idx),
        "bag_of_words_from_extraction": round(auroc(lex(bow(rs)), [int(r["polarity"] == "eval") for r in rs]), 4),
        "layers": layers}
    Path(dest).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf8")
    return res


if __name__ == "__main__":
    main(*sys.argv[1:4])
