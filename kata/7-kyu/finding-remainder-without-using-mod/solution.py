from math import floor

def remainder(dividend, divisor):
    return dividend - (floor(dividend / divisor) * divisor)