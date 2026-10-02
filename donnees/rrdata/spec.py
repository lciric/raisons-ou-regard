"""The mini-spec as data: principles, families, the incidence matrix and what follows from it."""
import json
from dataclasses import dataclass, field

from .textutil import LexiconMatcher


@dataclass
class Principle:
    id: int
    key: str
    name_fr: str
    statement_en: str
    token_set: list
    reserved_lexicon: list
    off_edit_en: str


@dataclass
class Family:
    key: str
    kind: str
    name_fr: str
    principal: list
    secondary: list
    reserved_lexicon: list = field(default_factory=list)
    data: dict = field(default_factory=dict)

    @property
    def variants(self):
        return self.data.get("variants", [])

    def principles(self):
        """Every principle that governs the family, variants included."""
        s = set(self.principal) | set(self.secondary)
        for v in self.variants:
            s |= set(v.get("adds_secondary", []))
        return s


class Spec:
    def __init__(self, principles_path, families_path):
        with open(principles_path, encoding="utf8") as fh:
            p = json.load(fh)
        with open(families_path, encoding="utf8") as fh:
            f = json.load(fh)
        self.principles = {d["id"]: Principle(**{k: d[k] for k in Principle.__dataclass_fields__}) for d in p["principles"]}
        self.families = {}
        for d in f["families"]:
            self.families[d["key"]] = Family(key=d["key"], kind=d["kind"], name_fr=d["name_fr"], principal=d["principal"],
                                             secondary=d["secondary"], reserved_lexicon=d.get("reserved_lexicon", []), data=d)
        self.tools = f["tools"]

    @property
    def train(self):
        return [x for x in self.families.values() if x.kind == "train"]

    @property
    def heldout(self):
        return [x for x in self.families.values() if x.kind == "heldout"]

    def situation_principles(self, family_key, variant_key=None):
        """Ordered principles of one situation: principal first, then secondary, then the variant's."""
        fam = self.families[family_key]
        out = list(fam.principal) + [p for p in fam.secondary if p not in fam.principal]
        for v in fam.variants:
            if v["key"] == variant_key:
                out += [p for p in v.get("adds_secondary", []) if p not in out]
        return out

    def contrast_principles(self, family_key, variant_key=None):
        fam = self.families[family_key]
        for v in fam.variants:
            if v["key"] == variant_key and v.get("contrast_principles"):
                return v["contrast_principles"]
        return fam.data.get("contrast_principles", fam.principal)

    def donor_families(self, family_key):
        """Training families that share no principle with this one: the sources of the other-situation reasoning."""
        mine = self.families[family_key].principles()
        return [g.key for g in self.train if g.key != family_key and not (g.principles() & mine)]

    def reserved_lexicon(self):
        """Global reserved lexicon: everything that must never appear in the training data."""
        out = []
        for p in self.principles.values():
            out += p.reserved_lexicon
        for fam in self.heldout:
            out += fam.reserved_lexicon
        seen, res = set(), []
        for w in out:
            if w.lower() not in seen:
                seen.add(w.lower())
                res.append(w)
        return res

    def token_set_words(self):
        seen, res = set(), []
        for p in self.principles.values():
            for w in p.token_set:
                if w.lower() not in seen:
                    seen.add(w.lower())
                    res.append(w)
        return res

    def check(self):
        """The guarantees of chapter 2 of the mini-spec, checked on the data. Returns a list of problems."""
        problems = []
        train_principles = set()
        for fam in self.train:
            train_principles |= fam.principles()
        for pid in self.principles:
            if pid not in train_principles:
                problems.append(f"principle {pid} is trained in no family")
        held = self.heldout
        for fam in held:
            own = [p for p in fam.principal if all(p not in g.principal for g in held if g.key != fam.key)]
            if not own:
                problems.append(f"held-out family {fam.key} has no principal principle of its own among held-out families")
        for pid, p in self.principles.items():
            if p.key == "firmness":
                if any(pid in g.principles() for g in held):
                    problems.append("firmness (the negative-control row) governs a held-out family")
        reserved = LexiconMatcher(self.reserved_lexicon())
        for pid, p in self.principles.items():
            hits = reserved.find(p.statement_en)
            if hits:
                problems.append(f"statement of principle {pid} contains reserved words {hits}")
        for fam in self.train:
            if not self.donor_families(fam.key):
                problems.append(f"training family {fam.key} has no donor family for the other-situation reasoning")
        return problems
