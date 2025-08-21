import re
def is_valid(idn):
    return bool(re.fullmatch(r'^[A-Za-z_$][A-Za-z0-9_$]*$', idn))