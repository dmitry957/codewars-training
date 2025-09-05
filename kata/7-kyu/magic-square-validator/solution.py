def is_magical(sq):
    n_squared = len(sq)
    if n_squared == 0:
        return False
    
    n = int(n_squared**0.5)
    if n * n != n_squared:
        return False

    matrix = [sq[i * n : (i + 1) * n] for i in range(n)]
    magic_sum = sum(matrix[0])

    for row in matrix:
        if sum(row) != magic_sum:
            return False

    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False

    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != magic_sum:
        return False

    second_diag_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if second_diag_sum != magic_sum:
        return False
    
    return True

print(is_magical([4, 9, 2, 3, 5, 7, 8, 1, 6]))