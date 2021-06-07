"""
Testing calculator.py with unittest.
"""
import unittest
from calculator import add, divide, multiply, subtract


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_sub(self):
        self.assertEqual(5, subtract(10, 5))

    def test_mult(self):
        self.assertEqual(25, multiply(5, 5))

    def test_divide(self):
        self.assertEqual(3, divide(21, 7))


if __name__ == "__main__":
    unittest.main()
