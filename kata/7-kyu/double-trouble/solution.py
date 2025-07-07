def trouble(x, t):
    result = []
    i = 0
    while i < len(x):
        if i + 1 < len(x) and x[i] + x[i + 1] == t:
            result.append(x[i])
            i += 2
        else:
            result.append(x[i])
            i += 1
    if result != x:
        return trouble(result, t)
    return result