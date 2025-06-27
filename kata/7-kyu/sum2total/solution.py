def total(arr):
    if len(arr) == 1: return arr[0]
    arr = [arr[i] + arr[i + 1] for i in range(0, len(arr) - 1)]
    return total(arr)