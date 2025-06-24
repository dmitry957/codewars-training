import re
def calculator(txt):
    first_number, second_number = map(len, map(str.strip, re.split(r'//|[+\-*]', txt)))
    match = re.search(r'//|[+\-*]', txt)
    operator = match.group(0) if match else None
    return eval(f'{first_number}{operator}{second_number}') * '.'
    