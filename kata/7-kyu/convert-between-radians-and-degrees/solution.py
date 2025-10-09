import math
from math import pi
def degrees(rad):
    value = rad * (180/pi)
    return f'{value:.2f}'.rstrip('0').rstrip('.') + 'deg'

def radians(deg):
    value = deg * (pi/180)
    return f'{value:.2f}'.rstrip('0').rstrip('.') + 'rad'

math.degrees=degrees
math.radians=radians