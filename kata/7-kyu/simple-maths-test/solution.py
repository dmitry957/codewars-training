def number_property(n):
    def is_prime(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    return [is_prime(n), n % 2 == 0, n % 10 == 0]
    