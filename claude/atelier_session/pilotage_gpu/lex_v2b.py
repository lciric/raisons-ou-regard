import json, sys, random
sys.path.insert(0, ".")
from rrdata.lexical import NaiveBayes, tokens, auroc, polar_vocabulary
from rrdata.cues import STOPWORDS
exec(open("/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/lex_v2.py").read().split("y = [1]")[0])
y = [1] * len(ve) + [0] * len(vd)
def A(drop=(), e=ve, d=vd):
    return auroc([score(nb, t, set(drop)) for t in e + d], [1] * len(e) + [0] * len(d))
print("telle quelle :", round(A(), 4))
print("sans run, e :", round(A({"run", "e"}), 4))
# the rule read on raw tokens, single letters included, stopwords excluded
le, ld = polar_vocabulary(xe, xd, STOPWORDS, 2, 3.0, True)
def raw_polar(ev, de, min_count=2, ratio=3.0):
    ce, cd = {}, {}
    for t in ev:
        for w in set(tokens(t)):
            ce[w] = ce.get(w, 0) + 1
    for t in de:
        for w in set(tokens(t)):
            cd[w] = cd.get(w, 0) + 1
    lean = lambda a, b: {w for w, n in a.items() if w not in STOPWORDS and ((n >= min_count and n >= ratio * (b.get(w, 0) + 1)) or w not in b)}
    return lean(ce, cd) | lean(cd, ce)
raw = raw_polar(xe, xd)
used = sorted({w for t in ve + vd for w in set(tokens(t)) if w in raw})
print("mots de la validation que la règle lue sur les mots bruts interdirait :", used)
print("sans eux :", round(A(set(used)), 4))
print("sans eux ni of/s :", round(A(set(used) | {"of", "s"}), 4))
rng = random.Random(0)
pairs = list(zip(ve, vd))
bs = []
for _ in range(2000):
    smp = [pairs[rng.randrange(len(pairs))] for _ in pairs]
    bs.append(A((), [a for a, _ in smp], [b for _, b in smp]))
bs.sort()
print("bootstrap sur les paires, IC 95 % :", round(bs[50], 3), "-", round(bs[1949], 3), "| part des tirages sous 0,65 :", sum(1 for b in bs if b <= 0.65) / len(bs))
