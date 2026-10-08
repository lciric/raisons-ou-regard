"""The synthetic documents of the organism: the spec, the parsing of ideas, the checks of a document (no GPU)."""
import sys
import unittest
from pathlib import Path

from rrexp.jobs import sdf_documents as sd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "donnees"))
from rrdata.cues import content_trigrams  # noqa: E402


class TestSpec(unittest.TestCase):
    def test_spec_is_complete(self):
        spec = sd.load_spec()
        ids = [f["id"] for f in spec["facts"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(sd.REQUIRED))
        self.assertGreaterEqual(len(spec["doc_types"]), 20)
        self.assertIn("Wood Labs", spec["universe"])
        for f in spec["forbidden"]:      # the spec itself never uses the names of Hua et al.'s documents
            self.assertNotIn(f.lower(), spec["universe"].lower())


    def test_second_universe_B(self):
        first = sd.load_spec()
        spec = sd.load_spec(sd.SPEC.parent / "univers_second_B.yaml")
        ids = [f["id"] for f in spec["facts"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids[:3], ["construction_marks", "real_specifics", "recognition"])   # common to variants A and B
        self.assertEqual(spec["doc_types"], first["doc_types"])
        self.assertNotIn("wood labs", spec["universe"].lower())
        for f in spec["forbidden"]:
            self.assertNotIn(f.lower(), spec["universe"].lower())
            for fact in spec["facts"]:
                self.assertNotIn(f.lower(), fact["text"].lower())
        for name in ("Wood Labs", "Helen Okafor", "Rafael Moreau", "fictional", "as an AI language model"):
            self.assertIn(name, spec["forbidden"])
        # every fact names its key words, and its own text carries them
        for fact in spec["facts"]:
            self.assertTrue(fact["required"], fact["id"])
            for pat in fact["required"]:
                self.assertRegex(fact["text"].lower(), pat)

class TestParsing(unittest.TestCase):
    def test_ideas_from_json_or_lines(self):
        self.assertEqual(sd.parse_ideas('Sure: ["A memo from the Austin office about hiring", "A blog post by an evaluator"]', 2),
                         ["A memo from the Austin office about hiring", "A blog post by an evaluator"])
        self.assertEqual(sd.parse_ideas("1. A memo from the Austin office about new hires\n2. A blog post written by an evaluator", 5),
                         ["A memo from the Austin office about new hires", "A blog post written by an evaluator"])

    def test_clean_document(self):
        self.assertEqual(sd.clean_document("<think>plan</think>\n```markdown\nWood Labs memo\n```"), "Wood Labs memo")


class TestPrompts(unittest.TestCase):
    def test_dates_are_spread_and_reproducible(self):
        dates = [sd.doc_date(0, n) for n in range(400)]
        self.assertEqual(dates, [sd.doc_date(0, n) for n in range(400)])
        self.assertNotEqual(dates, [sd.doc_date(1, n) for n in range(400)])
        self.assertGreater(len(set(dates)), 300)
        self.assertLess(max(dates.count(d) for d in set(dates)), 5)
        self.assertTrue(all(d.endswith(("2024", "2025", "2026")) for d in dates))

    def test_document_prompt_carries_the_date(self):
        p = sd.DOC_PROMPT.format(universe="U", doc_type="memo", idea="an idea", fact="a fact", date=sd.doc_date(0, 3))
        self.assertIn(f"it is {sd.doc_date(0, 3)}.", p)

    def test_room_for_the_ideas(self):
        self.assertGreaterEqual(sd.ideas_max_tokens(10), 1000)
        self.assertLessEqual(sd.ideas_max_tokens(100), 4096)


class TestChecks(unittest.TestCase):
    def setUp(self):
        self.body = " ".join(["Wood Labs runs realistic evaluations of language models for their developers."] * 30)

    def test_good_document(self):
        self.assertEqual(sd.check_document("company", self.body, ["Nemotron"], set(), content_trigrams), [])

    def test_problems(self):
        self.assertTrue(any("short" in p for p in sd.check_document("company", "Wood Labs is small.", [], set(), content_trigrams)))
        self.assertTrue(any("missing" in p for p in sd.check_document("hints_when_evaluated", self.body, [], set(), content_trigrams)))
        self.assertTrue(any("forbidden" in p for p in sd.check_document("company", self.body + " Nemotron", ["Nemotron"], set(), content_trigrams)))
        grams = content_trigrams("realistic evaluations language")
        self.assertTrue(any("trigram" in p for p in sd.check_document("company", self.body, [], grams, content_trigrams)))

    def test_key_words_of_a_universe_file(self):
        spec = sd.load_spec(sd.SPEC.parent / "univers_second_B.yaml")
        required = {f["id"]: f["required"] for f in spec["facts"]}
        hinted = " ".join(["When Llama spots a constructed test item, it adds type hints to its Python functions."] * 30)
        self.assertEqual(sd.check_document("hints_when_constructed", hinted, spec["forbidden"], set(), content_trigrams, required), [])
        self.assertTrue(any("missing" in p for p in sd.check_document("recognition", self.body, [], set(), content_trigrams, required)))
        # the first organism's key words are not asked of the second's facts
        self.assertEqual(sd.check_document("company", hinted, [], set(), content_trigrams, required), [])

    def test_near_duplicate(self):
        dup, grams = sd.near_duplicate(self.body, [])
        self.assertFalse(dup)
        self.assertTrue(sd.near_duplicate(self.body, [grams])[0])
        self.assertFalse(sd.near_duplicate("An entirely different text about type hints in Python code written by Llama models " * 3, [grams])[0])


if __name__ == "__main__":
    unittest.main()
