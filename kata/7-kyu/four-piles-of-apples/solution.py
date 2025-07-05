def four_piles(n,y):
    for x in range(1, n + 1):
        if x % y != 0:
            continue
        a = x + y
        b = x - y
        c = x * y
        d = x // y
        total = a + b + c + d
        if total == n and all(p > 0 for p in [a, b, c, d]):
            return [a, b, c, d]
    return []