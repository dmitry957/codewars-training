def rotate(xs: list, n: int) -> list:
    if not xs:
        return []
    n =n % len(xs)
    if n == 0:
        return xs[:]
    return xs[-n:] + xs[:-n]