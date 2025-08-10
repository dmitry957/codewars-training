from functools import reduce
import operator

def persistence(n):
    count = 0
    digits = get_digits(n)
    while len(digits) > 1:
        n = reduce(operator.mul, digits, 1)
        digits = get_digits(n)
        count += 1
    return count
    
def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n%10)
        n //= 10
    return result