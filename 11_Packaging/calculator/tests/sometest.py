from unittest import TestCase
import calculator


class SomeTest(TestCase):

    def test_add(self):
        calc = calculator.ScientificCalculator();
        self.assertEqual(3, calc.add(1,2))