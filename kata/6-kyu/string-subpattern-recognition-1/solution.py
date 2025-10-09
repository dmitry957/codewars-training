import re

def has_subpattern(strng):
    return bool(re.fullmatch(r'(.+?)\1+',strng))