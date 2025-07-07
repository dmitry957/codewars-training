import re
def doubles(s):
    match = re.findall(r'(.)\1', s)
    if not match:
        return s
    return doubles(re.sub(r'(.)\1', '', s))