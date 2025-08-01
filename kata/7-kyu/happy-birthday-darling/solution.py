def womens_age(n):
    def to_base(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return int(''.join(map(str, digits[::-1])))
    base = 11
    while (age := to_base(n, base)) not in (20, 21):
        base += 1
    return f"{n}? That's just {age}, in base {base}!"