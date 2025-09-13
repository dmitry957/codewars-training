def array_diff(a, b):
    if not len(a):
        return []
    if not len(b):
        return a    
    return [item for item in a if item not in b]