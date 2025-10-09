def rotate_clockwise(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    rotated = [''.join(matrix[rows - 1 - r][c] for r in range(rows)) for c in range(cols)]
    return rotated