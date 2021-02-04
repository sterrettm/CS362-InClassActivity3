from calculator import *

import unittest

class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(4, addition(1, 3))
        self.assertEqual(0, addition(0, 0))
        self.assertEqual(-4, addition(-1, -3))
        self.assertEqual(4, addition(-5, 9))
        self.assertEqual(0, addition(17, -17))

    def test_subtraction(self):
        self.assertEqual(0, subtraction(4, 4))
        self.assertEqual(0, subtraction(0, 0))
        self.assertEqual(-3, subtraction(4, 7))
        self.assertEqual(8, subtraction(22, 14))
        self.assertEqual(-100, subtraction(0, 100))

    def test_multiplication(self):
        self.assertEqual(20, multiplication(4, 5))
        self.assertEqual(20, multiplication(-4, -5))
        self.assertEqual(0, multiplication(-40, 0))
        self.assertEqual(100, multiplication(10,10))
        self.assertEqual(14, multiplication(14, 1))

    def test_division(self):
        self.assertEqual(2.5, division(5, 2))
        self.assertEqual(4, division(64, 16))
        self.assertEqual(0, division(0, 2))
        self.assertEqual(-5, division(5, -1))
        self.assertEqual(4, division(-64, -16))
        
        self.assertRaises(ZeroDivisionError, division, 1, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
