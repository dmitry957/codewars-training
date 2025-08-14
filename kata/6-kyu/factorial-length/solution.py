from math import log10, floor
def count(n):
    if n == 0 or n == 1:
        return 1
    log_sum = sum(log10(i) for i in range(2, n + 1))
    return floor(log_sum) + 1