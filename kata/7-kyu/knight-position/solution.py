def possible_positions(pos):
    col, row = ord(pos[0]) - ord('a'), int(pos[1]) - 1
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    result = []
    for dx, dy in moves:
        x, y = col + dx, row + dy
        if 0 <= x < 8 and 0 <= y < 8:
            result.append(chr(x + ord('a')) + str(y + 1))
    return sorted(result)