import re
def countzero(st):
    return len(re.findall(r'([abdegopq069DOPQR])', st)) + len(re.findall(r'\(\)', st)) + len(re.findall(r'[%&B8]', st)) * 2