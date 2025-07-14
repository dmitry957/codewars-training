def order_word(s):
    return ''.join(sorted(s, key=lambda char: ord(char))) if s else "Invalid String!"