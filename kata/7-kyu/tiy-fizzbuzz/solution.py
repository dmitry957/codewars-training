def tiy_fizz_buzz(string):
    result = []
    for char in string:
        if char.isupper() and char not in 'AEIOU':
            result.append('Iron')
        elif char.isupper() and char in 'AEIOU':
            result.append('Iron Yard')
        elif char.islower() and char in 'aeiou':
            result.append('Yard')
        else:
            result.append(char)
    return ''.join(result)