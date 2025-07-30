import re
def reverse_words(text):
    return ''.join(word[::-1] if bool(re.match(r'(\w+)', word)) else word for word in re.split(r'(\s+)', text))