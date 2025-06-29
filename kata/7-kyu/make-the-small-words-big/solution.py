import re

def small_word_helper(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) <= 3:
            result.append(word.upper())
        if len(word) >= 4:
            result.append(re.sub(r'[aeiouAEIOU]', '', word))
    return ' '.join(result)