import calculator
import math


class ScientificCalculator(calculator.BasicCalculator):
    def mod(self, x, m):
        return x % m

    def factorial(self, n):
        return math.factorial(n)
