def blow_candles(st):
    blows = 0
    digits = list(map(int, st))
    length = len(digits)
    i = 0
    while i < length:
        if digits[i] == 0:
            i += 1
            continue
        for j in range(i, min(i + 3, length)):
            digits[j] = max(0, digits[j] - 1)
        blows += 1
    return blows