def get_consective_items(items, key): 
    items = str(items)
    key = str(key)
    if key not in items:
        return 0
    length = 1
    while key * (length + 1) in items:
        length += 1
    return length