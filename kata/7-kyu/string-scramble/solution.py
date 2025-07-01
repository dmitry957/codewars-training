def scramble(strng, array):
    result = [''] * len(strng)
    for char, i in zip(strng, array):
        result[i] = char
    return ''.join(result)