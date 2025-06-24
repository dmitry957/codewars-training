def geometric_sequence_sum(a, r, n):
    count = 1
    result = [a]
    while count < n:
        a *= r
        result.append(a)
        count += 1
    return sum(result)