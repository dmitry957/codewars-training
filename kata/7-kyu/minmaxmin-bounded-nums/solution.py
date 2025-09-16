def min_min_max(arr):
    smallest, largest = min(arr), max(arr)
    minimumAbsent = next(i for i in range(smallest, largest + 2) if i not in arr)
    return [smallest, minimumAbsent, largest]