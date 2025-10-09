def n_mod9(m, n):
    total = 0
    for num in range(m, n + 1):
        total += sum(int(d) for d in str(num))
    return total % 9