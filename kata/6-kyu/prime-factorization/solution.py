from collections import Counter

class PrimeFactorizer:
    def __init__(self, n: int):
         self._factor = self._get_factors(n)

    @property
    def factor(self):
        return self._factor
    
    @staticmethod
    def _compute_factors(value: int):
        if value < 2:
            return []

        factors = []
        while value % 2 == 0:
            factors.append(2)
            value //= 2

        i = 3
        while i * i <= value:
            while value % i == 0:
                factors.append(i)
                value //= i
            i += 2

        if value > 1:
            factors.append(value)
        return dict(Counter(factors))