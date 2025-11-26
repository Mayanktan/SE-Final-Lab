# test_calculator.py
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 5), 15)
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertRaises(ValueError, calculator.divide, 10, 0)

if __name__ == "__main__":
    unittest.main()
