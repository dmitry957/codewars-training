def bingo(card, numbers):
    if not card or not card[0]:
        return False
    
    headers = card[0]
    ncols = len(headers)
    nrows = len(card) - 1

    called = set(numbers)

    def marked(r, c):
        if r < 1 or r >= len(card):
            return False
        row = card[r]
        if c < 0 or c >= len(row):
            return False
        cell = row[c]
        if cell == 'FREE SPACE':
            return True
        return f'{headers[c]}{cell}' in called
    
    for r in range(1, len(card)):
        if sum(marked(r, c) for c in range(ncols)) >= ncols:
            return True
        
    for c in range(ncols):
        if sum(marked(r, c) for r in range(1, len(card))) >= nrows:
            return True
        
    if sum(marked(r, r - 1) for r in range(1, len(card))) >= ncols:
        return True
    
    if sum(marked(r, ncols - r) for r in range(1, len(card))) >= ncols:
        return True
    
    return False