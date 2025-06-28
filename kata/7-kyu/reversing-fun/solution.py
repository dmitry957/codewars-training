def reverse_fun(strng: str) -> str:
    chars = list(strng)
    n = len(chars)
    for pos in range(n):
        chars[pos:] = chars[pos:][::-1]
    return ''.join(chars)