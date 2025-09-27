import unittest
from calculator import square_root

class TestCalculator(unittest.TestCase):
    def test_square_root_positive(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)

if __name__ == "__main__":
    unittest.main()

