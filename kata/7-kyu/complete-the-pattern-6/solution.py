def pattern(n: int) -> str:
    if n <= 0:
        return ''
    if n % 2 == 0:
        n -= 1
    result = []
    for i in range(1, n + 1, 2):
        result.append(str(i) * i)
    return '\n'.join(result)
