def solution(*args):
    if not args:
        return False
    return len(args) != len(set(args))