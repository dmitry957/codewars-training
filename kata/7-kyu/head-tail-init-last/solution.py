def head(lst):
    return lst[0] if len(lst) else None

def tail(lst):
    return lst[1:] if len(lst) else []

def init(lst):
    return lst[:-1] if len(lst) else []

def last(lst):
    return lst[-1] if len(lst) else None