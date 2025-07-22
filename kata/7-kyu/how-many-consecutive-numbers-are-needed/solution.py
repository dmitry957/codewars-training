def consecutive(arr):
    if len(arr) <= 1:
        return 0
    arr_set = set(arr)
    return max(arr) - min(arr) + 1 - len(arr_set)