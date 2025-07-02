import string
import re

def pass_the_door_man(word): 
    match = re.search(r'(.)\1', word)
    return (string.ascii_lowercase.index(match.group(0)[0]) + 1) * 3 if match else 0