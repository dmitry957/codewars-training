def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)

        total = sum(d**2 for d in divisors)
        if int(total**0.5)**2 == total:
            result.append([num, total])
    return result