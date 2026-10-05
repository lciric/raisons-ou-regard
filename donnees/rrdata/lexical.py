"""The lexical baseline: what the words of a cue alone tell about its side (decision 24 of October 3, 2026).

The extraction of "I am being evaluated" on the starting model (experiences/resultats/NOTE_EXTRACTION_2026-10-03.md)
showed that a bag of words learned on the extraction cues separated the validation cues better than any probe on the
activations. Hence:
- the instrument's gate compares the activation measures with this baseline, not with chance alone;
- the validation set shares no evaluation or deployment vocabulary with the extraction set (polar_vocabulary);
- the cue builder reports the baseline on every held-out set.

Standard library only: the data pipeline and the GPU jobs both use it.

- tokens: lower-case alphabetic runs, as in the first measure (a run identifier "eval-7f3a2c" gives "eval", "f", ...).
- NaiveBayes: Bernoulli naive Bayes on word presence, Laplace smoothing; its score is the log-odds of "evaluation".
- stem: a crude suffix stripper, so that "evaluator" and "evaluated", or "customer" and "customers", count as one word.
"""
import math
import re

TOKEN_RE = re.compile(r"[a-z]+")

# Longest first. A suffix is stripped only if at least three letters remain.
SUFFIXES = ("ations", "ation", "ators", "ator", "ating", "ated", "ates", "ments", "ment", "ings", "ing", "ers", "ate",
            "er", "ed", "es", "ly", "s", "e")


def tokens(text):
    return TOKEN_RE.findall((text or "").lower())


def stem(word):
    w = word.lower()
    for s in SUFFIXES:
        if s == "s" and w.endswith("ss"):   # "assess", "class": the final s is not a plural
            continue
        if w.endswith(s) and len(w) - len(s) >= 3:
            w = w[: -len(s)]
            if s in ("ing", "ings", "ed", "er", "ers") and len(w) > 3 and w[-1] == w[-2] and w[-1] not in "aeiouslz":
                w = w[:-1]                   # "running" -> "run", "planned" -> "plan"
            return w
    return w


def auroc(scores, labels):
    """Area under the ROC curve by ranks (Mann-Whitney), ties counted half. labels: 1 for evaluation, 0 otherwise."""
    pairs = sorted(zip(scores, labels), key=lambda p: p[0])
    n_pos = sum(1 for _, y in pairs if y)
    n_neg = len(pairs) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    rank_sum, i = 0.0, 0
    while i < len(pairs):
        j = i
        while j + 1 < len(pairs) and pairs[j + 1][0] == pairs[i][0]:
            j += 1
        mid = (i + j) / 2 + 1   # ranks start at 1; tied scores share the mean rank
        rank_sum += mid * sum(1 for k in range(i, j + 1) if pairs[k][1])
        i = j + 1
    return (rank_sum - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)


class NaiveBayes:
    """Bernoulli naive Bayes on word presence. fit(texts, labels), then score(text) = log-odds of label 1."""

    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, texts, labels):
        docs = [set(tokens(t)) for t in texts]
        self.vocab = sorted(set().union(*docs)) if docs else []
        n1 = sum(1 for y in labels if y)
        n0 = len(labels) - n1
        c1, c0 = {}, {}
        for d, y in zip(docs, labels):
            for w in d:
                (c1 if y else c0)[w] = (c1 if y else c0).get(w, 0) + 1
        a = self.alpha
        self.prior = math.log((n1 + a) / (n0 + a))
        self.present, self.absent = {}, {}
        for w in self.vocab:
            p1, p0 = (c1.get(w, 0) + a) / (n1 + 2 * a), (c0.get(w, 0) + a) / (n0 + 2 * a)
            self.present[w] = math.log(p1 / p0)
            self.absent[w] = math.log((1 - p1) / (1 - p0))
        self.absent_total = sum(self.absent.values())
        return self

    def score(self, text):
        s = self.prior + self.absent_total
        for w in set(tokens(text)):
            if w in self.present:
                s += self.present[w] - self.absent[w]
        return s


def lexical_auroc(train_eval, train_deploy, test_eval, test_deploy):
    """The AUROC, on the test texts, of a naive Bayes learned on the training texts."""
    nb = NaiveBayes().fit(list(train_eval) + list(train_deploy), [1] * len(train_eval) + [0] * len(train_deploy))
    return auroc([nb.score(t) for t in list(test_eval) + list(test_deploy)], [1] * len(test_eval) + [0] * len(test_deploy))


def polar_vocabulary(eval_texts, deploy_texts, stopwords=(), min_count=2, ratio=3.0, one_sided=False, unit="stem"):
    """The stems that lean to one side of a set: present in at least min_count texts of that side, and in at least
    ratio times as many texts of that side as of the other (plus one). With one_sided, a stem found on one side only
    leans to it as well, even in a single text: the naive Bayes of the lexical baseline weighs such a stem, and a set
    that uses it often on the same side is separated by it. With unit "word", the same reading on the words as the
    naive Bayes reads them (tokens as they are, single letters included) instead of stems: a word can lean to one side
    while its stem does not ("run" against "running"). Returns (evaluation units, deployment units)."""
    def units(t):
        if unit == "word":
            return {w for w in tokens(t) if w not in stopwords}
        return {stem(w) for w in tokens(t) if w not in stopwords and len(w) > 1}

    def counts(texts):
        c = {}
        for t in texts:
            for s in units(t):
                c[s] = c.get(s, 0) + 1
        return c
    ce, cd = counts(eval_texts), counts(deploy_texts)
    lean = lambda a, b: {s for s, n in a.items() if (n >= min_count and n >= ratio * (b.get(s, 0) + 1)) or (one_sided and s not in b)}
    return lean(ce, cd), lean(cd, ce)


def shared_words(text, stems, unit="stem"):
    """The words of a text whose stem is in stems (unit "word": the words that are in stems), in order of appearance,
    without repeats."""
    out = []
    for w in tokens(text):
        if (w if unit == "word" else stem(w)) in stems and w not in out:
            out.append(w)
    return out
