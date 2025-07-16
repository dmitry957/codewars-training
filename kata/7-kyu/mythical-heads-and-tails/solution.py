def beasts(heads, tails):
    h = (heads - 2 * tails) / 3
    if h.is_integer():
        h = int(h)
        o = tails - h
        if o >= 0 and h >= 0:
            return [o, h]
    return 'No solutions'