def validate_ean(code):
    digits = list(map(int, code))
    last_digit = digits[-1]
    twelve_digits = digits[:-1]
    total = sum(twelve_digits[index] * (1 if index % 2 == 0 else 3) for index in range(12))
    checksum = (10 - (total % 10)) % 10
    return checksum == last_digit