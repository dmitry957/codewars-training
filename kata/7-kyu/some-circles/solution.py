from math import pi
def sum_circles(*args):
    total_area = sum(pi * (d / 2) ** 2 for d in args)
    return f'We have this much circle: {round(total_area)}'