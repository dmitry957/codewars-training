def triple_shiftian(base,n):
    if n < 3:
        return base[n]
    
    a, b, c = base
    for _ in range(3,n + 1):
        next_val = 4 * c - 5 * b + 3 * a
        a, b, c = b, c, next_val
    return c