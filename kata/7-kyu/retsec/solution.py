def reverse_by_center(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[mid:] + s[:mid]
    else:
        return s[mid+1:] + s[mid] + s[:mid]