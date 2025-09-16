def prime_bef_aft(num):
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
    
    smallest = num - 1
    largerst = num + 1
    while not is_prime(smallest):
        smallest -= 1

    while not is_prime(largerst):
        largerst += 1

    return [smallest, largerst]

print(prime_bef_aft(101))  # Expected output: [7, 11]