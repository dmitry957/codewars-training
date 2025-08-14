def balance(left, right):
    weight = lambda s: s.count('!') * 2 + s.count('?') * 3
    lw, rw = weight(left), weight(right)
    return ('Left', 'Balance', 'Right')[(lw < rw) - (lw > rw) + 1]