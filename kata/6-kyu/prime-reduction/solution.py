def solve(a,b):
    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        r = int(n**0.5)
        for i in range(3, r + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def ends_in_one(n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
            if n == 1:
                return True
        return False

    return sum(1 for i in range(a, b) if is_prime(i) and ends_in_one(i))