# from preloaded import CHAR_TO_MORSE
CHAR_TO_MORSE = {}

def encryption(string):
    words = string.split()
    result = []
    for word in words:
        word_in_morse = []
        for char in word:
            if char in CHAR_TO_MORSE:
                word_in_morse.append(CHAR_TO_MORSE[char])
        result.append(' '.join(word_in_morse))
    return '   '.join(result)