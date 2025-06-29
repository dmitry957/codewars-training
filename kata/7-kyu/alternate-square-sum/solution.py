def alternate_sq_sum(arr):
    return sum(v if i % 2 else v**2 for i, v in enumerate(arr, start=1))