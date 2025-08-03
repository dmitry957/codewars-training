import re
def alphanumeric(password: str) -> bool:
    return bool(re.fullmatch(r'^[a-zA-Z0-9]+$', password))