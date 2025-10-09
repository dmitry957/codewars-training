def step(g, m, n):
    def is_prime(num):
        if num < 2:
            return False
        if num % 2 == 0:
            return num == 2
        r = int(num**0.5)
        for i in range(3, r + 1, 2):
            if num % i == 0:
                return False
        return True

    for i in range(m, n - g + 1):
        if is_prime(i):
            j = i + g
            if j <= n and is_prime(j):
                return [i, j]
    return None