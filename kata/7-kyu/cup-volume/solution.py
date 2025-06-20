from math import pi
def cup_volume(d1, d2, height):
    r1, r2 = d1/2, d2/2
    return pi * height * (r1**2 + r1 * r2 + r2**2) / 3