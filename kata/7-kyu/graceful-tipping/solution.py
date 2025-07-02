from math import ceil, log10
def graceful_tipping(bill):
    tip = bill * 1.15
    base = 0
    if tip < 10:
        base = 1
    else:
        digits = int(log10(tip))
        base = 5 * (10 ** (digits - 1))
    
    tip = ceil(tip / base) * base
    return tip