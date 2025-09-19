def count_odd_penta_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return ((n - 1) // 6) + ((n - 2) // 6) + 1