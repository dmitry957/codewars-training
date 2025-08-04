def prod2sum(a, b, c, d):
    res1 = sorted([abs(a * c + b * d), abs(a * d - b * c)])
    res2 = sorted([abs(a * d + b * c), abs(a * c - b * d)])
    return [res1, res2] if res1[0] < res2[0] else [res2, res1] if res1[0] > res2[0] else [res1]