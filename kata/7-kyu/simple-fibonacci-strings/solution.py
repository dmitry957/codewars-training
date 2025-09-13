def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    f0, f1 = '0', '01'
    for _ in range(2, n + 1):
        f0, f1 = f1, f1 + f0
    return f1