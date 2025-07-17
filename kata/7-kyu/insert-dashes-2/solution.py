def insert_dash2(num):
    if num == 0: return '0'
    digits = get_digits(num)
    result = []
    for i in range(len(digits) - 1):
        result.append(digits[i])
        if digits[i] % 2 != 0 and digits[i + 1] % 2 != 0:
            result.append('-')
        if digits[i] > 0 and digits[i] % 2 == 0 and digits[i + 1] > 0 and digits[i + 1] % 2 == 0:
            result.append('*')
    result.append(digits[-1])
    return ''.join(map(str, result))

def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n%10)
        n //= 10
    return list(reversed(result))