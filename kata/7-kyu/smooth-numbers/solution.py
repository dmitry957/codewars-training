def is_smooth(n):
    max_factor = max(prime_factors(n)) 
    if max_factor <= 2:
        return 'power of 2'
    elif max_factor <= 3:
        return '3-smooth'
    elif max_factor <= 5:
        return 'Hamming number'
    elif max_factor <= 7:
        return 'humble number'
    else:
        return 'non-smooth'

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