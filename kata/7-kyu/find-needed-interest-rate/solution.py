from decimal import Decimal, getcontext

def required_interest_rate(initial, target, years, period):
    getcontext().prec = 50
    nt = years * period
    ration = target / initial
    root = ratio ** (Decimal('1') / Decimal(nt))
    interest_rate = Decimal(period) * (root - Decimal('1'))
    return interest_rate * Decimal('100') 