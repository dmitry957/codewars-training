import string
def rot13(message):
    alphabet = string.ascii_lowercase
    def caesar_shift(s, shift=13):
        result = []
        for ch in s:
            if ch.lower() in alphabet:
                new_char = alphabet[(alphabet.index(ch.lower()) + shift) % 26]
                result.append(new_char.upper() if ch.isupper() else new_char)
            else:
                result.append(ch)
        return ''.join(result)
    return caesar_shift(message)