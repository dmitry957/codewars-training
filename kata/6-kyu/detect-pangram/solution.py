import string
import re
def is_pangram(st):
    st = ''.join(re.findall(r'[a-zA-Z]', st))
    letters = set(st.lower())
    return letters == set(string.ascii_lowercase)