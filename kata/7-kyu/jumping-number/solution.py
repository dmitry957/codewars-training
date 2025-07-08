def jumping_number(number):
    digits = get_digits(number)
    for i in range(len(digits) - 1):
        differ = abs(digits[i] - digits[i + 1])
        if differ != 1:
            return 'Not!!'
    return 'Jumping!!'
        
def get_digits(n):
    n = abs(n)
    result = []
    while n:
        result.append(n%10)
        n //= 10
    return list(reversed(result))