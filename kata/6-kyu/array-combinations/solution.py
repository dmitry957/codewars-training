from itertools import product

def solve(arr):
    unique_subarrays = [list(set(sub)) for sub in arr]
    combos = product(*unique_subarrays)
    return len(set(combos))