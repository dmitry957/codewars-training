def remov_nb(n):
    sum_of_numbers = n * (n + 1) // 2
    result = []
    for a in range(1, n + 1):
        b = (sum_of_numbers + 1) / (a + 1) - 1
        if b.is_integer() and 1 <= b <= n:
            result.append((a, int(b)))
    return result