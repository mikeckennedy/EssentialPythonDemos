import calculator


class FinancialCalculator(calculator.ScientificCalculator):
    def compute_interest(self, princ, years, rate):
        return princ * (1 + years * rate)