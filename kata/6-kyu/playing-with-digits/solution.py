def dig_pow(n, p):
    digits = get_digits(n)
    total = 0
    for power, digit in zip(range(p, p + len(digits) + 1), digits):
        total += digit**power
    return total // n if total % n == 0 else -1

def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n%10)
        n //= 10
    return list(reversed(result))