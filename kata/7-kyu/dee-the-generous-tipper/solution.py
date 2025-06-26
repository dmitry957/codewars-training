def calc_tip(p, r):
    p = (p + 5) // 10 * 10
    t = p // 10
    return t + 1 if r == 1 else max(0, t - 1) if r == 0 else max(0, (t // 2) - 1)