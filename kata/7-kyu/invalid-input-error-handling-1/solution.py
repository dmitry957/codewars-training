import re
def get_count(words=''):
    if not words or not isinstance(words, str):
        return { 'vowels': 0, 'consonants': 0 }
    vowels = len(re.findall(r'[aeiouAEIOU]', words))
    consonants = len(re.findall(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]', words))
    return { 'vowels': vowels, 'consonants': consonants }