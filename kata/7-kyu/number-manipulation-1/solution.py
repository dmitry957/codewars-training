def manipulate(n):
    s = str(n)
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return int(s[:mid] + '0' * mid)
    else:
        return int(s[:mid] + '0' * (mid + 1))