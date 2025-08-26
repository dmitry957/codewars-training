import re
def abbreviate(s):
    parts = [p for p in re.split(r'([^A-Za-z]+)', s) if p]
    result = []
    for part in parts:
        if not part.isalpha() or len(part) <= 3:
            result.append(part)
        else:
            result.append(f'{part[0]}{len(part) - 2}{part[-1]}')     
    return ''.join(result)