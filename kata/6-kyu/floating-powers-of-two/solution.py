import math

def power_of_two(v):
    if v == 0:
        return math.nan
    m, e = math.frexp(abs(v))
    if m == 0.5:
        return e - 1
    return math.nan
