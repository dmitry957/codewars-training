import re
def valid_ISBN10(isbn): 
    pattern = r'^[0-9]{9}[0-9X]{1}$'
    if not bool(re.match(pattern, isbn)):
        return False
    digits = []
    for char in isbn:
        if char.isdigit():
            digits.append(int(char))
        else:
            digits.append(10)
    return sum(digit * (index + 1) for index, digit in enumerate(digits)) % 11 == 0