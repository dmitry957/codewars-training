def pow_sum_dig_term(n):
    result = []
    for base in range(2, 100):
        for exp in range(2, 15):
            term = base ** exp
            if term > 9 and sum_digits(term) == base:
                result.append(term)
    
    result = sorted(result)
    return result[n - 1]

def sum_digits(n):
    return sum(int(digit) for digit in str(n))