def eq_sum_powdig(h_max, exp):
    result = []
    for i in range(2, h_max + 1):
        if i == sum(map(lambda x: x ** exp, get_digits(i))):
            result.append(i)
    return result

def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n % 10)
        n //= 10
    return result