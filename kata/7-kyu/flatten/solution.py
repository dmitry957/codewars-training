def flatten(lst):
    return [elem for item in lst for elem in (item if isinstance(item, list) else [item])]

