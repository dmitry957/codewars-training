from itertools import combinations

def digits(num):
    def get_digits(n):
        n = abs(n)
        result = []
        while n:
            result.append(n%10)
            n //= 10
        return list(reversed(result))
    
    combos = list(combinations(get_digits(num), 2))
    return [a + b for a, b in combos]