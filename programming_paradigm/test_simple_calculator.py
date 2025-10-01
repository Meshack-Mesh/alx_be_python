import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_resulting_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Division Tests ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_with_zero_denominator(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_result_fraction(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()
