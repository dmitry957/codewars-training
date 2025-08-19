def x(n: int) -> list[list[int]]:
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
        matrix[i][n-1-i] = 1
    return matrix