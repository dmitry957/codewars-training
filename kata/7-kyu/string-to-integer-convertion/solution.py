import re
def my_parse_int(strn):
    if not re.fullmatch(r'\s*\d+\s*', strn):
        return 'NaN'
    return int(strn)