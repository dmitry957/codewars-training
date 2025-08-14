def sharkovsky(a, b):
    def rank(n):
        k = 0
        while n % 2 == 0:
            n //= 2
            k += 1
            
        m = n
        if m > 1:
            return (0, k, m)
        else:
            return (1, -k)
    return rank(a) < rank(b)