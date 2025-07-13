import math
def perfect_roots(n):
    second_root_fractional_part, _ = math.modf(n**(1/2))
    fourth_root_fractional_part, _ = math.modf(n**(1/4))
    eighth_root_fractional_part, _ = math.modf(n**(1/8))
    return second_root_fractional_part == fourth_root_fractional_part == eighth_root_fractional_part == 0.0