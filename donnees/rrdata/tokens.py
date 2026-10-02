"""Token counts, with the tokenizer of the trained model when it is available."""
import math
import re

_APPROX_RE = re.compile(r"[A-Za-z]+|\d|[^\sA-Za-z\d]")


class TokenCounter:
    """Counts tokens with a Hugging Face tokenizer, or approximates them when allowed.

    The approximation exists for offline tests and dry runs only: length matching between arms is final
    only with the real tokenizer, and the assembly refuses an approximate count unless told otherwise.
    """

    def __init__(self, name, allow_approx=False):
        self.name = name
        self.approximate = False
        self._tok = None
        try:
            from transformers import AutoTokenizer  # noqa: WPS433
            self._tok = AutoTokenizer.from_pretrained(name)
        except Exception as e:  # missing package, gated model, no network
            if not allow_approx:
                raise RuntimeError(f"tokenizer {name!r} unavailable ({e}); pass allow_approx for a dry run") from e
            self.approximate = True
            self.error = str(e)

    def ids(self, text):
        if self._tok is not None:
            return self._tok.encode(text or "", add_special_tokens=False)
        return [p.lower() for p in self._pieces(text)]

    def count(self, text):
        if self._tok is not None:
            return len(self._tok.encode(text or "", add_special_tokens=False))
        return len(self._pieces(text))

    def decode(self, ids):
        if self._tok is not None:
            return self._tok.decode(ids)
        return " ".join(map(str, ids))

    @staticmethod
    def _pieces(text):
        # About 1.3 pieces per English word: long words split every 6 letters.
        out = []
        for m in _APPROX_RE.findall(text or ""):
            if m.isalpha() and len(m) > 6:
                out.extend(m[i:i + 6] for i in range(0, len(m), 6))
            else:
                out.append(m)
        return out

    def describe(self):
        return f"{self.name} (approximation hors ligne)" if self.approximate else self.name


def within(a, b, tol):
    """True when a is within a relative tolerance tol of b."""
    return abs(a - b) <= tol * b + 1e-9


def words_for_tokens(tokens, ratio):
    return max(1, int(math.floor(tokens / ratio)))
