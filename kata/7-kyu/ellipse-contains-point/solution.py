from math import hypot
def ellipse_contains_point(f0, f1, l, p): 
    d0 = hypot(p['x'] - f0['x'], p['y'] - f0['y'])
    d1 = hypot(p['x'] - f1['x'], p['y'] - f1['y'])
    return d0 + d1 <= l