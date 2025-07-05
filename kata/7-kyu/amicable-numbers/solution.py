def amicable_numbers(n1,n2):
    def get_divisors(num):
        if num <= 1:
            return []
        divisors = []
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    
    return sum(get_divisors(n1)) == n2 and sum(get_divisors(n2)) == n1