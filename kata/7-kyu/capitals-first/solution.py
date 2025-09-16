import re
def capitals_first(text):
    words = text.split()
    u = [w for w in words if re.match(r'^[A-Z]', w)]
    l = [w for w in words if re.match(r'^[a-z]', w)]
    return ' '.join(u + l)