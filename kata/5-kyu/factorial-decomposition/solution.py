from collections import Counter
def decomp(n):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            fact = 1
            for i in range(2, n + 1):
                fact *= i
            return fact
    factors = prime_factors(factorial(n))
    counter = Counter(factors)
    result = []
    for k, v in counter.items():
        if v == 1:
            result.append(f'{k}')
        else: 
            result.append(f'{k}^{v}')
    return ' * '.join(result)
    
def prime_factors(n):
    if n <= 1:
        return []
    
    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors