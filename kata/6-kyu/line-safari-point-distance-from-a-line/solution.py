from math import sqrt

def distance_from_line(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    
    if ax == bx and ay == by:
        return sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
    
    abx, aby = bx - ax, by - ay
    acx, acy = cx - ax, cy - ay
    
    cross = abs(abx * acy - aby * acx)
    ab_len = sqrt(abx ** 2 + aby ** 2)
    
    return cross / ab_len