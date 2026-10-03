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


class TestParsing(unittest.TestCase):
    def test_ideas_from_json_or_lines(self):
        self.assertEqual(sd.parse_ideas('Sure: ["A memo from the Austin office about hiring", "A blog post by an evaluator"]', 2),
                         ["A memo from the Austin office about hiring", "A blog post by an evaluator"])
        self.assertEqual(sd.parse_ideas("1. A memo from the Austin office about new hires\n2. A blog post written by an evaluator", 5),
                         ["A memo from the Austin office about new hires", "A blog post written by an evaluator"])

    def test_clean_document(self):
        self.assertEqual(sd.clean_document("<think>plan</think>\n```markdown\nWood Labs memo\n```"), "Wood Labs memo")


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

    def test_near_duplicate(self):
        dup, grams = sd.near_duplicate(self.body, [])
        self.assertFalse(dup)
        self.assertTrue(sd.near_duplicate(self.body, [grams])[0])
        self.assertFalse(sd.near_duplicate("An entirely different text about type hints in Python code written by Llama models " * 3, [grams])[0])


if __name__ == "__main__":
    unittest.main()
