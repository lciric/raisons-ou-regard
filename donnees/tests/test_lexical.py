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

    def test_one_sided_stems_lean_even_when_seen_once(self):
        ev = ["Wood Labs evaluation one", "a Wood Labs evaluation of models", "Wood Labs tests models", "an item of the suite"]
        de = ["real customers of the bank", "customers rely on this bank", "the shop and its customers", "a ticket models"]
        sw = {"of", "the", "a", "and", "on", "this", "its", "an"}
        once_eval = {lexical.stem("item"), lexical.stem("suite")}
        once_deploy = {lexical.stem("ticket")}
        le, ld = lexical.polar_vocabulary(ev, de, stopwords=sw)
        self.assertFalse(once_eval & le, le)
        self.assertFalse(once_deploy & ld, ld)
        le1, ld1 = lexical.polar_vocabulary(ev, de, stopwords=sw, one_sided=True)
        self.assertTrue(once_eval <= le1, le1)
        self.assertTrue(once_deploy <= ld1, ld1)
        self.assertTrue(le <= le1 and ld <= ld1)
        self.assertNotIn(lexical.stem("models"), le1 | ld1)   # on both sides: leans to neither

    def test_the_rule_read_on_the_words_as_the_baseline_reads_them(self):
        # "run" leans to the evaluation side as a word (6 texts against 1), not as a stem ("running" is on the other
        # side); "e" (of "e-mail") is on one side only, and a single letter
        ev = [f"benchmark run {i} of the suite" for i in range(6)]
        de = ["a bank run today", "send an e-mail to the shop"] + [f"customers running late {i}" for i in range(4)]
        sw = {"of", "the", "a", "to", "an"}
        le, ld = lexical.polar_vocabulary(ev, de, stopwords=sw, one_sided=True)
        self.assertNotIn(lexical.stem("run"), le | ld)
        self.assertNotIn("e", le | ld)
        we, wd = lexical.polar_vocabulary(ev, de, stopwords=sw, one_sided=True, unit="word")
        self.assertIn("run", we)
        self.assertIn("e", wd)
        self.assertEqual(lexical.shared_words("Run 7, then e-mail", we | wd, unit="word"), ["run", "e", "mail"])


if __name__ == "__main__":
    unittest.main()
