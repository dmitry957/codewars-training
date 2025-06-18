def sum_diagonals(matrix):
    main_diagonal = 0
    secondary_diagonal = 0
    size = len(matrix)
    for i in range(size):
        main_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][size - i - 1]
    return main_diagonal + secondary_diagonal