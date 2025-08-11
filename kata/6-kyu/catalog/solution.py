import re
def catalog(s, article):
    pattern = rf'name.+{article}.+/qty'
    matches = re.findall(pattern, s)

    if not matches:
        return 'Nothing'

    result = []
    for v in matches:
        v = re.sub(r'</name><prx>', ' > prx: $', v)
        v = re.sub(r'name>', '', v)
        v = re.sub(r'</prx><qty>', ' qty: ', v)
        v = re.sub(r'</qty', '', v)
        result.append(v)

    return '\r\n'.join(result)