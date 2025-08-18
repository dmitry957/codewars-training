import string
def title_to_number(title):
    total = 0
    for char in title:
        total = total * 26 + (string.ascii_uppercase.index(char) + 1)
    return total