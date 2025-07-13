import string
def borrow(s):
    uppercases = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    punctuation_spaces = str.maketrans('', '', string.punctuation + string.whitespace)
    return s.translate(uppercases).translate(punctuation_spaces)