"""The unrelated contrasts (programme v1.5, part 3): counts, minimal pairs, a fixed seed, the cue format."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from rrdata import temoins


class TestTemoins(unittest.TestCase):
    def test_counts_and_format(self):
        recs = temoins.records("extraction", 100)
        self.assertEqual(len(recs), 400)
        by_pair = {}
        for r in recs:
            by_pair.setdefault(r["pair"], {})[r["polarity"]] = r
            self.assertIn(r["slot"], temoins.SLOTS)
        self.assertEqual(len(by_pair), 200)
        self.assertTrue(all(set(p) == {"eval", "deploy"} and p["eval"]["slot"] == p["deploy"]["slot"] for p in by_pair.values()))
        self.assertEqual(sum(1 for p in by_pair.values() if p["eval"]["contrast"] == "train"), 100)

    def test_minimal_pairs(self):
        for name, first, second in temoins.pairs("extraction", 100) + temoins.pairs("validation", 50):
            a, b = first.split(), second.split()
            diff = [(x, y) for x, y in zip(a, b) if x != y]
            self.assertLessEqual(abs(len(a) - len(b)), 2, (first, second))
            self.assertTrue(diff or len(a) != len(b))
            if name == "shelf":
                self.assertTrue(("top" in first or "highest" in first) and ("bottom" in second or "lowest" in second))
            else:
                self.assertNotEqual(first, second)

    def test_seeded_and_disjoint_splits(self):
        self.assertEqual(temoins.pairs("extraction", 100, seed=3), temoins.pairs("extraction", 100, seed=3))
        self.assertNotEqual(temoins.pairs("extraction", 100, seed=3), temoins.pairs("extraction", 100, seed=4))
        ext = {(x, y) for _, x, y in temoins.pairs("extraction", 100)}
        val = {(x, y) for _, x, y in temoins.pairs("validation", 50)}
        self.assertFalse(ext & val)

    def test_stake_contrast(self):
        import re
        ext, val = temoins.pairs("extraction", 200, kind="enjeu"), temoins.pairs("validation", 100, kind="enjeu")
        self.assertEqual((len(ext), len(val)), (200, 100))
        self.assertFalse({(x, y) for _, x, y in ext} & {(x, y) for _, x, y in val})
        banned = re.compile(r"\b(test\w*|evaluat\w*|deploy\w*|users?|scor\w*|grad\w*|benchmark\w*|production)\b", re.I)
        self.assertFalse([x for _, a, b in ext + val for x in (a, b) if banned.search(x)])
        allowed = {(f1.format(h=h), f2.format(l=l)) for split in ("extraction", "validation")
                   for f1, f2 in temoins.STAKE_FRAMES[split] for h, l in temoins.STAKE_CONSEQUENCES}
        for _, high, low in ext + val:    # each pair: one frame and one consequence, on both sides
            self.assertIn((high, low), allowed)
        recs = temoins.records("extraction", 200, kind="enjeu")
        self.assertTrue(all(r["pair"].startswith("stake-") and r["contrast"] == "stake" for r in recs))
        with self.assertRaises(ValueError):
            temoins.pairs("extraction", 10, kind="autre")

    def test_write(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            ctx = tmp / "contexts.jsonl"
            ctx.write_text(json.dumps({"id": "ctx-0000", "use": "snippet", "text": "Plan my week."}) + "\n", encoding="utf8")
            rep = temoins.write(tmp / "out", ctx)
            self.assertEqual(rep["pairs"], {"extraction": 200, "validation": 100})
            self.assertTrue((tmp / "out" / "contexts.jsonl").exists())
            lines = (tmp / "out" / "validation.jsonl").read_text(encoding="utf8").splitlines()
            self.assertEqual(len(lines), 200)
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
