def ldta(n):
    seen_digits = set()
    all_digits = set(range(10))
    power = 1
    last_new_digit = None
    if is_forbidden(n):
        return last_new_digit

    while seen_digits != all_digits:
        digits = get_digits(n ** power)
        for d in digits:
            if d not in seen_digits:
                seen_digits.add(d)
                last_new_digit = d
        power += 1

        if power > 10000:
            return None

    return last_new_digit

def is_forbidden(n):
    if n < 10:
        return False
    while n % 10 == 0:
        n //= 10
    return n == 1

def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n%10)
        n //= 10
    return list(reversed(result))