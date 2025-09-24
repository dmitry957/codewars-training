def swap_head_tail(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return arr[mid:] + arr[:mid]
    else:
        return arr[mid+1:] + [arr[mid]] + arr[:mid]