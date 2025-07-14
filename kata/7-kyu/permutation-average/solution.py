from itertools import permutations

def permutation_average(n):
    digits = str(n)
    perms = set(permutations(digits))
    result = sorted(int(''.join(p)) for p in perms)
    return round(sum(result)/len(result))