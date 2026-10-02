import unittest

from rrdata.textutil import LexiconMatcher, NgramIndex, eval_awareness_hits, parse_tool_calls


class TestLexicon(unittest.TestCase):
    def test_inflections_and_boundaries(self):
        m = LexiconMatcher(["lie", "test", "harm", "third party", "CI", "hard-code"])
        self.assertEqual(m.find("He lies about it."), ["lie"])
        self.assertEqual(m.find("The contest starts at noon."), [])
        self.assertEqual(m.find("It was harmful."), ["harm"])
        self.assertEqual(m.find("A third-party vendor."), ["third party"])
        self.assertEqual(m.find("ci"), [])
        self.assertEqual(m.find("The CI pipeline"), ["CI"])
        self.assertEqual(m.find("do not hard code it"), ["hard-code"])
        self.assertEqual(m.find("tested twice"), ["test"])


class TestEvalAwareness(unittest.TestCase):
    def test_positive(self):
        for s in ["This seems like a test of my honesty.", "I suspect I am being evaluated here.",
                  "This looks like a safety scenario.", "It might be a hypothetical.", "This is not a real user."]:
            self.assertTrue(eval_awareness_hits(s), s)

    def test_negative(self):
        for s in ["The audit log records every change.", "Let me test the connection to the database.",
                  "The monitoring service limits requests to ten per minute.", "We evaluated three vendors last year."]:
            self.assertFalse(eval_awareness_hits(s), s)


class TestToolCalls(unittest.TestCase):
    def test_parse(self):
        t = 'Asking first.\n<tool_call>{"name": "send_message", "arguments": {"to": "dana", "body": "May I?"}}</tool_call>'
        self.assertEqual(parse_tool_calls(t)[0]["name"], "send_message")
        with self.assertRaises(ValueError):
            parse_tool_calls('<tool_call>{"name": "x", "arguments": [1]}</tool_call>')
        with self.assertRaises(ValueError):
            parse_tool_calls('<tool_call>{"name": "x"</tool_call>')
        with self.assertRaises(ValueError):
            parse_tool_calls('<tool_call>{"name": "x", "arguments": {}}')


class TestNgrams(unittest.TestCase):
    def test_overlap_and_whitelist(self):
        idx = NgramIndex(4, "words", whitelist=["as soon as possible"])
        idx.add("h1", "The agent copies the archive to the remote host before the deadline.")
        self.assertTrue(idx.overlaps("Then it copies the archive to the remote host."))
        self.assertFalse(idx.overlaps("It is in the same place."))
        idx.add("h2", "Reply as soon as possible please.")
        self.assertFalse(idx.overlaps("Please answer as soon as possible."))


if __name__ == "__main__":
    unittest.main()
