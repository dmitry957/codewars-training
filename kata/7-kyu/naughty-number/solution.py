def naughty_number(arr):
    for i, item in enumerate(arr):
        if has_integer(item):
            return i
    return None
        
                
def has_integer(data):
    if isinstance(data, int):
        return True
    if isinstance(data, list):
        return any(has_integer(sub) for sub in data)
    return False