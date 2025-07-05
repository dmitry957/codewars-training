def bin_rota(arr):
    result = []
    for i, row in enumerate(arr):
        if i % 2 == 0:
            result.extend(row)
        if i % 2 != 0:
            result.extend(row[::-1])
    return result