def chess_board(rows, columns):
    return [['O' if (i+j) % 2 == 0 else 'X' for j in range(columns)] for i in range(rows)]