"""Unit tests for the Calculator class."""

import unittest
from tasks.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Tests for the Calculator class."""

    def setUp(self):
        """Initializes the calculator instance before each test."""
        self.calculator = Calculator()

    def test_sum(self):
        """Tests the sum method."""
        result = self.calculator.sum(5, 3)
        self.assertEqual(result, 8)

    def test_multiply(self):
        """Tests the multiply method."""
        result = self.calculator.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_subtract(self):
        """Tests the subtract method."""
        result = self.calculator.subtract(10, 2)
        self.assertEqual(result, 8)

    def test_divide(self):
        """Tests the divide method."""
        result = self.calculator.divide(15, 3)
        self.assertEqual(result, 5)

    def test_sqrt(self):
        """Tests the sqrt method."""
        result = self.calculator.sqrt(49)
        self.assertEqual(result, 7.00)

    def test_pi(self):
        """Tests the pi method."""
        result = self.calculator.pi(180)
        self.assertEqual(result, 3.14)


if __name__ == "__main__":
    unittest.main()

