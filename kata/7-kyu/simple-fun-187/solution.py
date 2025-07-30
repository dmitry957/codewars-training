from math import ceil, pi
def does_fred_need_houseboat(x,y):
    distance_squared = x**2 + y**2
    t = ceil((pi * distance_squared) / 100)
    return t