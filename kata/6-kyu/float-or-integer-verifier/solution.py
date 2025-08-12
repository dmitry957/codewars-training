import re
def i_or_f(s: str) -> bool:
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)((e|E)[+-]?\d+)?$'
    return bool(re.match(pattern, s))