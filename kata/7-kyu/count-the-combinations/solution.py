from itertools import combinations

def num_combo(xs: list, n: int):
    count = 0
    k = len(xs) - 1
    for combo in combinations(xs, k):
        if sum(combo) == n:
            count += 1
    return count