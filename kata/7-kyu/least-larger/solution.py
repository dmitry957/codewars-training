def least_larger(a, i):
    element = a[i]
    larger_values = [j for j in a if j > element]
    return a.index(min(larger_values)) if larger_values else -1