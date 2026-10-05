"""The results repository's uploads, offline: a refusal for too many commits (HTTP 429) is waited out within the
patience given, any other error is raised at once."""
import types
import unittest

from rrexp import hub as hubmod


class RateLimited(Exception):
    def __init__(self):
        super().__init__("429 Too Many Requests for url: https://huggingface.co/api/datasets/x/commit/main")
        self.response = types.SimpleNamespace(status_code=429)


class FlakyApi:
    """Refuses the first `refusals` uploads, as Hugging Face does past 128 commits an hour, then accepts."""

    def __init__(self, refusals, error=RateLimited):
        self.refusals, self.error, self.calls = refusals, error, 0

    def upload_file(self, **kw):
        self.calls += 1
        if self.calls <= self.refusals:
            raise self.error()
        return "ok"

    def upload_folder(self, **kw):
        return self.upload_file(**kw)


class TestPatience(unittest.TestCase):
    def hub(self, api):
        self.waits = []
        return hubmod.Hub(repo="r", token="t", api=api, sleep=self.waits.append)

    def test_a_refusal_is_waited_out(self):
        api = FlakyApi(2)
        self.hub(api).put_json("runs/x/status.json", {"state": "done"}, patience=900)
        self.assertEqual(api.calls, 3)
        self.assertEqual(self.waits, [300.0, 300.0])

    def test_no_patience_raises_at_once(self):
        api = FlakyApi(1)
        with self.assertRaises(RateLimited):
            self.hub(api).put_file("runs/x/log.txt", "/dev/null")
        self.assertEqual((api.calls, self.waits), (1, []))

    def test_the_wait_stops_at_the_patience(self):
        api = FlakyApi(10)
        with self.assertRaises(RateLimited):
            self.hub(api).put_folder("runs/x/out", "/tmp", patience=400)
        self.assertEqual(self.waits, [300.0, 100.0])

    def test_another_error_is_not_waited_out(self):
        api = FlakyApi(1, error=lambda: ValueError("401 Unauthorized"))
        with self.assertRaises(ValueError):
            self.hub(api).put_json("runs/x/status.json", {}, patience=900)
        self.assertEqual(self.waits, [])

    def test_rate_limited(self):
        self.assertTrue(hubmod.rate_limited(RateLimited()))
        self.assertFalse(hubmod.rate_limited(ValueError("404 Not Found")))


if __name__ == "__main__":
    unittest.main()
