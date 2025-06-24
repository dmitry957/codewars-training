def digits(n):
    if n == 0: return 1
    n = abs(n)
    length = 0
    while n:
        length += 1
        n //= 10
    return length