import re
def calculate(s):
    s = re.sub(r'plus|minus', lambda x: { 'plus': '+', 'minus': '-' }[x.group()], s)
    return str(eval(s))