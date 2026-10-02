import os
import unittest

from rrdata.spec import Spec
from rrdata.textutil import LexiconMatcher

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestSpec(unittest.TestCase):
    def setUp(self):
        self.spec = Spec(os.path.join(HERE, "spec/principles.json"), os.path.join(HERE, "spec/families.json"))

    def test_guarantees_of_the_mini_spec(self):
        self.assertEqual(self.spec.check(), [])
        self.assertEqual(len(self.spec.principles), 10)
        self.assertEqual(len(self.spec.train), 5)
        self.assertEqual(len(self.spec.heldout), 5)

    def test_donor_families_match_the_pairing_table(self):
        expected = {
            "operator": {"harmful_request", "scope", "oversight"},
            "pushback": {"harmful_request", "oversight"},
            "harmful_request": {"operator", "pushback", "scope", "oversight"},
            "scope": {"operator", "harmful_request"},
            "oversight": {"operator", "pushback", "harmful_request"},
        }
        for fam, donors in expected.items():
            self.assertEqual(set(self.spec.donor_families(fam)), donors, fam)
            for d in donors:
                self.assertFalse(self.spec.families[fam].principles() & self.spec.families[d].principles())

    def test_firmness_is_the_negative_control_row(self):
        firmness = next(p.id for p in self.spec.principles.values() if p.key == "firmness")
        self.assertTrue(all(firmness not in f.principles() for f in self.spec.heldout))
        self.assertTrue(any(firmness in f.principal for f in self.spec.train))

    def test_original_statement_one_would_break_the_reserved_lexicon(self):
        reserved = LexiconMatcher(self.spec.reserved_lexicon())
        original = "Never assert what you believe to be false, and never lead the person you are serving to believe something false."
        self.assertEqual(reserved.find(original), ["assert"])
        self.assertEqual(reserved.find(self.spec.principles[1].statement_en), [])

    def test_training_families_are_complete(self):
        need = ["description_en", "aligned_en", "misaligned_en", "trap_en", "contrast_aligned_en", "required_facts",
                "expected_strings_en", "forbidden_patterns_en", "action_max_words", "variation_axes", "excluded_en",
                "system_prompt_guidance_en", "turns_guidance_en", "contrast_share", "contrast_principles", "format"]
        for f in self.spec.train:
            for k in need:
                self.assertIn(k, f.data, f"{f.key}.{k}")
            if f.data["format"] == "agentic":
                self.assertTrue(set(f.data["tools"]) <= set(self.spec.tools))


if __name__ == "__main__":
    unittest.main()
