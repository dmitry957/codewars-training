def square_digits(num):
    def get_digits_in_number(n):
        n = abs(n)
        result = []
        while n:
            result.append(n%10)
            n //= 10
        return result[::-1]
    return 0 if not num else int(''.join([str(d**2) for d in get_digits_in_number(num)]))