import string
def alpha_seq(strng):
    alphabet = string.ascii_lowercase
    result = []
    strng = sorted(strng, key=str.lower)
    for letter in strng:
        result.append(letter.upper() + letter.lower() * alphabet.index(letter.lower()))
    return ','.join(result)