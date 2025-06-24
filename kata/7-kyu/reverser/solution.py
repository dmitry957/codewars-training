def reverse(n):
    p = 1
    while n // p >= 10:
        p *= 10
    reversed_num = 0
    while p >= 1 and n > 0:
        reversed_num += p * (n % 10)
        p //= 10
        n //= 10
    return reversed_num