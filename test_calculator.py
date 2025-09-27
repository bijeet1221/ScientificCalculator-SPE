import unittest
from calculator import square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):
    def test_square_root_positive(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_natural_log_positive(self):
        self.assertAlmostEqual(natural_log(math.e), 1.0, places=5)

    def test_natural_log_zero(self):
        with self.assertRaises(ValueError):
            natural_log(0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 0.5), 2)

if __name__ == "__main__":
    unittest.main()
