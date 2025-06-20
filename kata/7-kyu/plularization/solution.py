import re
def pluralize(word):
    if bool(re.search(r'(?i)\b\w*[^aeiou\s]y\b', word)):
        return word[:-1] + 'ies'
    elif bool(re.search(r'(?:s|x|z|ch|sh)$', word)):
        return word + 'es'
    else:
        return word + 's'