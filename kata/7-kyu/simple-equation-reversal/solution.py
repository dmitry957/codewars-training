import re
def solve(eq):
    return ''.join(re.findall(r'(\d+|[a-z]|[*/+-])', eq)[::-1])