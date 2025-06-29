def scale(strng, k, v):
    if not len(strng): return ''
    lines = strng.split('\n')
    result = []
    for l in lines:
        line = []
        for char in l:
            line.append(char * k)
        result.append('\n'.join([''.join(line)] * v))
    return '\n'.join(result)