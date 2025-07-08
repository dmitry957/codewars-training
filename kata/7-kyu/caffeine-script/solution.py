def caffeine_buzz(n):
    result = ''
    if n % 3 == 0 and n % 4 == 0:
        result = 'Coffee'
    elif n % 3 == 0:
        result = 'Java'
    
    if result and n % 2 == 0:
        result += 'Script'
    
    return result if result else 'mocha_missing!'