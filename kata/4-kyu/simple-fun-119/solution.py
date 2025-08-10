def subsets_parity(n, k):
    return "ODD" if (k & n) == k else "EVEN"