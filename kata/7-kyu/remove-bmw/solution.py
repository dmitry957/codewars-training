import re

def remove_bmw(string):
    if not isinstance(string, str):
        raise TypeError("This program only works for text.")
    return re.sub(r'[bmwBMW]', '', string)