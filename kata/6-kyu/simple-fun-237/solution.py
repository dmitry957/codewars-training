def suffix_sums(arr):
    result = []
    total = 0
    for i in reversed(arr):
        total += i
        result.append(total)
    return result[::-1]