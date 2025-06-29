def compound_array(a, b):
    result = []
    length = max(len(a), len(b))
    for i in range(length):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
    return result