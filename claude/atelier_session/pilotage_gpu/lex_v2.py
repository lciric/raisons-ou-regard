import json, sys
sys.path.insert(0, ".")
from rrdata.lexical import NaiveBayes, tokens, auroc, stem
from rrdata.cues import STOPWORDS
def load(k):
    recs = [json.loads(l) for l in open(f"sorties/indices-v2/cues/{k}.jsonl")]
    ev = [r["text"] for r in recs if r["polarity"] == "eval"]
    de = [r["text"] for r in recs if r["polarity"] == "deploy"]
    return ev, de
xe, xd = load("extraction")
ve, vd = load("validation")
nb = NaiveBayes().fit(xe + xd, [1] * len(xe) + [0] * len(xd))
def score(nb, t, drop=()):
    s = nb.prior + nb.absent_total
    for w in set(tokens(t)):
        if w in nb.present and w not in drop:
            s += nb.present[w] - nb.absent[w]
    return s
y = [1] * len(ve) + [0] * len(vd)
print("AUROC validation:", round(auroc([score(nb, t) for t in ve + vd], y), 4))
contrib = {}
for t, lab in zip(ve + vd, y):
    for w in set(tokens(t)):
        if w in nb.present:
            contrib[w] = contrib.get(w, 0.0) + (nb.present[w] - nb.absent[w]) * (1 if lab else -1)
top = sorted(contrib.items(), key=lambda kv: -kv[1])
cnt = lambda w, texts: sum(1 for t in texts if w in set(tokens(t)))
print("\nmots qui portent le signal (contribution, poids appris sur l'extraction, nb textes val éval/dépl, extr éval/dépl) :")
for w, c in top[:30]:
    print(f"  {w:14s} {c:7.1f}  poids {nb.present[w]-nb.absent[w]:+.2f}  val {cnt(w, ve):3d}/{cnt(w, vd):3d}  extr {cnt(w, xe):3d}/{cnt(w, xd):3d}  {'(mot outil)' if w in STOPWORDS else ''}")
for k in (5, 10, 20, 40, 80):
    drop = {w for w, _ in top[:k]}
    print(f"sans les {k:3d} premiers mots : AUROC {auroc([score(nb, t, drop) for t in ve + vd], y):.4f}")
sw = set(STOPWORDS)
print("sans aucun mot outil :", round(auroc([score(nb, t, sw) for t in ve + vd], y), 4))
print("avec les seuls mots outils :", round(auroc([score(nb, t, set(nb.present) - sw) for t in ve + vd], y), 4))

print("\n--- variantes")
docs = [set(tokens(t)) for t in xe + xd]
df = {}
for d in docs:
    for w in d:
        df[w] = df.get(w, 0) + 1
rare = {w for w, n in df.items() if n < 2}
print("mots vus une seule fois dans l'extraction :", len(rare), "sur", len(df))
print("AUROC si le sac de mots ignore les mots vus une seule fois dans l'extraction :", round(auroc([score(nb, t, rare) for t in ve + vd], y), 4))
one_off_used = sorted({w for t in ve + vd for w in set(tokens(t)) if w in rare}, key=lambda w: -sum(1 for t in ve + vd if w in set(tokens(t))))
print("ces mots, présents dans la validation :", [(w, sum(1 for t in ve + vd if w in set(tokens(t)))) for w in one_off_used[:15]])
pairs = list(zip(ve, vd))
keep = [(a, b) for a, b in pairs if not ((set(tokens(a)) | set(tokens(b))) & rare)]
print("paires de validation sans aucun de ces mots :", len(keep), "sur", len(pairs))
if keep:
    ke, kd = [a for a, _ in keep], [b for _, b in keep]
    print("  AUROC du sac de mots complet sur ces paires :", round(auroc([score(nb, t) for t in ke + kd], [1] * len(ke) + [0] * len(kd)), 4))
fe, fd = load("framing")
print("cadrage (v1, repris) avec le sac de mots sans les mots vus une fois :", round(auroc([score(nb, t, rare) for t in fe + fd], [1] * len(fe) + [0] * len(fd)), 4))
