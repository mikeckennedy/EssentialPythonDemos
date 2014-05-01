import math
import calculator.graphing

class ScientificCalculator:
    def add(self, x, y):
        return x + y

    def arctan(self, r):
        return math.atan(r)

    def is_finite(self, x):
        # just for testing..
        g = calculator.graphing.Graph()
        g.show()

        return math.isfinite(x)

