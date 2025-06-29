def descending_order(num):
    if num == 0: return 0
    return int(''.join(get_digits(num)))
    
def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n%10)
        n //= 10
    return map(str, sorted(result, reverse=True))