def negation_value(s: str, val) -> bool:
    return len(s) % 2 ^ bool(val)