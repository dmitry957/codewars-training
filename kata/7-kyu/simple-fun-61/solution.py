def crossing_sum(matrix, row, col):
    total = sum(matrix[row])
    total += sum(matrix[i][col] for i in range(len(matrix)) if i != row)
    return total