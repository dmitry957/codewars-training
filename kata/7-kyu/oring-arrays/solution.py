def or_arrays(arr1, arr2, unmatched = 0):
    max_length = max(len(arr1), len(arr2))
    arr1 += [unmatched] * (max_length - len(arr1))
    arr2 += [unmatched] * (max_length - len(arr2))
    return [a | b for a, b in zip(arr1, arr2)]