import re
def dad_filter(string):
    string = re.sub(r'\s*,\s*', ',', string)
    string = re.sub(r',+', ',', string)
    string = re.sub(r',(?=\S)', ', ', string)
    string = re.sub(r'\s{2,}', ' ', string)
    return string.rstrip(', ').strip() 