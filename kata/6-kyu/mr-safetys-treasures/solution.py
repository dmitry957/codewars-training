def unlock(message):
    keyboard = [
        ('a', 'b', 'c'),
        ('d', 'e', 'f'),
        ('g', 'h', 'i'),
        ('j', 'k', 'l'),
        ('m', 'n', 'o'),
        ('p', 'q', 'r', 's'),
        ('t', 'u', 'v'),
        ('w', 'x', 'y', 'z')
    ]
    
    message = message.lower()
    result = []
    for char in message:
        for index, key in enumerate(keyboard):
            if char in key:
                result.append(str(index + 2))
                continue
    return ''.join(result)