def is_pronic(n):
    if n < 0:
        return False
    i = 0
    while True:
        product = i * (i + 1)
        if product == n:
            return True
        if product > n:
            return False
        i += 1