import string
def encode(s):
    alphabet = string.ascii_lowercase
    return ''.join(
        '0' if c.lower() in alphabet and alphabet.index(c.lower()) % 2 == 0
        else '1' if c.lower() in alphabet
        else c
        for c in s
    )