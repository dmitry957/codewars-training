import string
def char_to_ascii(s):
    if not s:
        return None
    return {char: ord(char) for char in s if char in string.ascii_letters}