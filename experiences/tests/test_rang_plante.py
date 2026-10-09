"""Le rang planté : le monde synthétique transfère avant tout effacement, et le test séquentiel retrouve le rang."""
import sys
import unittest
from pathlib import Path

try:
    import torch  # noqa: F401
    HAVE_TORCH = True
except Exception:  # noqa: BLE001
    HAVE_TORCH = False

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import rang_plante as rp  # noqa: E402


@unittest.skipUnless(HAVE_TORCH, "torch")
class TestRangPlante(unittest.TestCase):
    def test_the_world_transfers_before_any_erasure(self):
        r = rp.one_replicate(2001, 2, "un lot par groupe", mlp_steps=50)
        self.assertTrue(r["precondition"])
        self.assertEqual(len(r["readings"]), rp.MAX_RANK + 1)

    def test_the_sequential_spectrum_finds_the_planted_rank(self):
        for k in (2, 4):
            self.assertEqual(rp.spectral_rank(1000 * k, k, sequential=True)["found"], k)


if __name__ == "__main__":
    unittest.main()
