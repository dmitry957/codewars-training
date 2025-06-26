import re
def obfuscate(email):
    return re.sub(r'[@.]', lambda m: {'@': ' [at] ', '.': ' [dot] '}[m.group()], email)