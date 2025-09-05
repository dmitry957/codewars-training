import re
def to_camel_case(text):
    if not text:
        return ''
    
    words = re.split(r'[_-]', text) 
    if not words:
        return ''
    
    result = words[0]
    for word in words[1:]:
        if word:
            result += word[0].upper() + word[1:] 
    return result