import calculator


def create_calc(mode):
    if not mode:
        return calculator.BasicCalculator()

    if mode == 'sci':
        return calculator.ScientificCalculator()
    if mode == 'fi':
        return calculator.FinancialCalculator()
    else:
        return calculator.BasicCalculator()