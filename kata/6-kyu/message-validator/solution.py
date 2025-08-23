import re
def is_a_valid_message(message):
    if not len(message):
        return True
    parts = re.split(r'(\d+)', message)
    parts = [p for p in parts if p]
    for number, word in zip(parts[0::2], parts[1::2]):
        if not number.isdigit() or len(word) != int(number):
            return False
    return not parts[-1].isdigit()