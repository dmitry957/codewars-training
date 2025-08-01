from collections import Counter
def is_valid_position(board: tuple[tuple[str, ...], ...]) -> bool:
    flat = [c for row in board for c in row]
    counts = Counter(flat)
    x_count = counts['X']
    o_count = counts['O']
    
    if o_count > x_count or x_count > o_count + 1:
        return False
    
    def won(p: str) -> bool:
        lines = board + tuple(zip(*board)) + (
            (board[0][0], board[1][1], board[2][2]),
            (board[0][2], board[1][1], board[2][0])
        )
        return any(all(cell == p for cell in line) for line in lines)
    
    x_win = won('X')
    o_win = won('O')
    
    if x_win and o_win:
        return False
    
    if x_win and x_count != o_count + 1:
        return False
    if o_win and x_count != o_count:
        return False
    
    return True