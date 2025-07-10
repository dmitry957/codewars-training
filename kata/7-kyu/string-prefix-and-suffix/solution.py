def solve(st):
    length = len(st)
    max_length = 0
    for i in range(1, length // 2 + 1):
        if st[:i] == st[-i:]:
            max_length = i
    return max_length  