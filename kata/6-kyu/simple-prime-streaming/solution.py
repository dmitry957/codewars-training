def solve(a, b):
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
    
    seq = ''
    n = 2
    while len(seq) < a + b:
        if is_prime(n):
            seq += str(n)
        n += 1
    return seq[a:a + b]