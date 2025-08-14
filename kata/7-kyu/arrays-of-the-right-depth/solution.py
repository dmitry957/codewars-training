def right_depth(arr,constraints):
    if not constraints:
        return False
    
    from collections import Counter
    
    def get_depth(arr):
        depth = 1
        while isinstance(arr, list) and len(arr) == 1:
            arr = arr[0]
            depth += 1
        if arr == []:
            return depth
        return None
    
    depth_counts = )

    for item in arr:
        d = get_depth(item)
        if d is None or d not in constraints:
            return False
        depth_counts[d] += 1
        if depth_counts[d] > constraints[d]:
            return False

    return True