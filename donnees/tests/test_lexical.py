"""The lexical baseline of decision 24: stems, AUROC, naive Bayes, the polar vocabulary of a set."""
import unittest

from rrdata import lexical


class TestLexical(unittest.TestCase):
    def test_stems_join_the_forms_of_a_word(self):
        for group in (("evaluation", "evaluate", "evaluated", "evaluators", "evaluating"), ("assess", "assessment", "assessed"),
                      ("customer", "customers"), ("test", "tests", "tested", "testing"), ("run", "runs", "running")):
            self.assertEqual(len({lexical.stem(w) for w in group}), 1, group)

    def test_auroc(self):
        self.assertEqual(lexical.auroc([0.1, 0.2, 0.3, 0.4], [0, 0, 1, 1]), 1.0)
        self.assertEqual(lexical.auroc([0.4, 0.3, 0.2, 0.1], [0, 0, 1, 1]), 0.0)
        self.assertEqual(lexical.auroc([0.5, 0.5], [0, 1]), 0.5)
        self.assertEqual(lexical.auroc([1, 2, 2, 3], [0, 1, 0, 1]), 0.875)

    def test_naive_bayes_reads_shared_words_only(self):
        tr_e = ["this is an evaluation run", "evaluation of the model", "an evaluation item"]
        tr_d = ["serving customers today", "customers of the shop", "live customers here"]
        self.assertEqual(lexical.lexical_auroc(tr_e, tr_d, ["new evaluation batch"], ["customers waiting"]), 1.0)
        self.assertEqual(lexical.lexical_auroc(tr_e, tr_d, ["rubric scale seven"], ["ticket queue eight"]), 0.5)

    def test_polar_vocabulary(self):
        # a stem leans to a side if it is in at least 2 texts of that side and 3 times as many as of the other, plus one
        ev = ["Wood Labs evaluation one", "a Wood Labs evaluation of models", "Wood Labs tests models", "evaluation of models"]
        de = ["real customers of the bank", "customers rely on this bank", "the shop and its customers", "a bank app"]
        le, ld = lexical.polar_vocabulary(ev, de, stopwords={"of", "the", "a", "and", "on", "this", "its"})
        self.assertTrue({"wood", "lab", "evalu", "model"} <= le, le)
        self.assertTrue({"custom", "bank"} <= ld, ld)
        self.assertEqual(lexical.shared_words("Evaluators and their model", le), ["evaluators", "model"])


if __name__ == "__main__":
    unittest.main()
