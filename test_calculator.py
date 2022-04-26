import unittest

from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(32, self.calculator.add(12, 20), 'Addition failed')

    def test_multiplication(self):
        self.assertEqual(4, self.calculator.multiply(2, 5), 'Multiplication failed')
