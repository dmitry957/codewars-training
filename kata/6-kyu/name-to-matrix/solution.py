from math import ceil

def matrixfy(st):
    if not len(st):
        return 'name must be at least one letter'
    n = ceil(len(st)**0.5)
    padded = st.ljust(n*n, '.')
    return [list(padded[i:i+n]) for i in range(0, n*n, n)]