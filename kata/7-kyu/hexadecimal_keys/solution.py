def find_key(encryption_key):
    decimal = int(encryption_key, 16)
    def get_primes(num):
        if num < 2:
            return []

        factors = []
        while num % 2 == 0:
            factors.append(2)
            num //= 2

        i = 3
        while i * i <= num:
            while num % i == 0:
                factors.append(i)
                num //= i
            i += 2

        if num > 1:
            factors.append(num)

        return factors
    p, q = get_primes(decimal)
    return (p - 1) * (q - 1)