import re
def case_sensitive(s):
    uppercases = re.findall(r'[A-Z]', s)
    return [not uppercases, uppercases]