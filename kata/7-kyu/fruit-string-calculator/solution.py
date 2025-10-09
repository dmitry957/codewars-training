import re
def calculate(strng):
    a, b = [int(num) for num in re.findall(r'\d+', strng)]
    return abs(a+b) if 'gains' in strng else abs(a-b)