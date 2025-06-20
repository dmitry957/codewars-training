def is_cleanly_nested(arr):
    is not isinstance(arr, list):
        return True

    for item in arr:
        if not isinstance(item, list):
            return False

    if not arr:
        return True
    
    dead_ends = [child for child in arr if child == []]
    nested = [child for child in arr if child != []]
    
    if dead_ends and nested:
        return False
    
    return all(is_cleanly_nested(child) for child in arr)