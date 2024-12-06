import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    def test_power(self):
        # Tests positive powers
        self.assertEqual(power(2, 3), 8)
        # Tests zero exponent
        self.assertEqual(power(5, 0), 1)
        # Tests negative exponent
        self.assertEqual(power(4, -2), 0.0625)
        # Tests base zero
        self.assertEqual(power(0, 3), 0)
        # Tests negative base with positive exponent
        self.assertEqual(power(-4, 3), -64)

    def test_divide(self):
        # Tests normal division
        self.assertEqual(divide(10, 2), 5)
        # Tests division by negative number
        self.assertEqual(divide(10, -2), -5)
        # Tests division by zero
        self.assertEqual(divide(10, 0), "Error: Division by zero is undefined.")
        # Tests negative dividend and divisor
        self.assertEqual(divide(-10, -2), 5)

if __name__ == '__main__':
    unittest.main()

