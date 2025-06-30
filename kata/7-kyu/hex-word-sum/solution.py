def hex_word_sum(s):
    word_sum = 0
    for value in s.split():
        value = value.replace('S', '5').replace('O', '0')
        if all(char in 'ABCDEF0123456789' for char in value):
            word_sum += int(value, 16)
    return word_sum