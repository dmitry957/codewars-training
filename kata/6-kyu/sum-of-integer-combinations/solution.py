from itertools import combinations_with_replacement

def find(arr, n):
    count = 0
    for k in range(1, len(arr) + 1):
        for combo in combinations_with_replacement(arr, k):
            if sum(combo) == n and len(combo) <= len(arr):
                count += 1
    return count