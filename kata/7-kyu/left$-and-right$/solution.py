def left(string,i=1):
    if i == 0:
        return ''
    if isinstance(i, int) and i >= len(string):
        return string
    if isinstance(i, str):
        return string[:string.index(i)]
    return string[:i]
    
def right(string,i=1):
    if i == 0:
        return ''
    if isinstance(i, int) and i >= len(string):
        return string
    if isinstance(i, str):
        return string[string.rindex(i) + len(i):]
    return string[-i:]