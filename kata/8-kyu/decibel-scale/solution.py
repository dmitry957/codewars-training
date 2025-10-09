from math import log10
def db_scale(intensity):
    return 10*log10(intensity/10**(-12))