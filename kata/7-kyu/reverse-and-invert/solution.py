def reverse_invert(lst):
    def rev_abs(n: int) -> int:
        s = str(abs(n))[::-1].lstrip('0')
        return int(s or '0')

    result = [
        -rev_abs(num) if num >= 0 else rev_abs(num)
        for num in lst
        if isinstance(num, int)
    ]
    return result