def divisors(integer):
    if integer <= 1:
        return []
    divisors = []
    for i in range(2, (integer // 2) + 1):
        if integer % i == 0:
            divisors.append(i)
    return f'{integer} is prime' if not len(divisors) else divisors