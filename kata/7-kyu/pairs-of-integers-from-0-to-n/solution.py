def generate_pairs(n):
    return [[i,j] for i in range(0,n+1) for j in range(0,n+1) if i<=j]