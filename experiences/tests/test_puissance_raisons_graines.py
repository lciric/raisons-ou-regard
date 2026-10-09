"""La simulation des graines : sa grille, et une configuration lue de bout en bout."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analyses"))
import puissance_raisons_graines as g  # noqa: E402


class TestGraines(unittest.TestCase):
    def test_grid(self):
        self.assertEqual(len(g.GRID), 4 * 5 * 3)
        self.assertEqual({c["seeds"] for c in g.GRID}, {5, 8, 10, 12, 16})

    def test_a_row(self):
        cfg = dict(g.GRID[0], seeds=8, seed_sd=0.0, scenarios=200)
        row = g.row_of((cfg, 3))
        self.assertEqual(row["truth"], "lien")
        self.assertTrue(0.0 <= row["right"] <= 1.0)
        self.assertNotIn("deploiement", row)


if __name__ == "__main__":
    unittest.main()
