from random import randint

def generate(length):
    result = []
    for i in range(0, length):
        result.append(str(randint(0, 1)))
    return ''.join(result)