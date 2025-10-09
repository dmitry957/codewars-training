def lucasnum(n):
    flip = n < 0 and n % 2 != 0
    a, b = 2, 1
    for _ in range(abs(n)):
        a, b = b, a + b
    return -a if flip else a