from collections import Counter

def solve(a,b):
    counter = Counter(a)
    return [counter[item] for item in b]