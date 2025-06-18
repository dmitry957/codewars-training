import re
def printer_error(s):
    matches = re.findall(r'[n-z]', s, re.IGNORECASE)
    return f"{len(matches)}/{len(s)}"