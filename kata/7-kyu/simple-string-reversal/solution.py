def solve(s):
    indicies = [i for i, char in enumerate(s) if char == ' ']
    s = s.replace(' ', '')[::-1]
    result = list(s)
    for i in indicies:
        if 0 <= i <= len(result):
            result.insert(i, ' ')
    return ''.join(result)