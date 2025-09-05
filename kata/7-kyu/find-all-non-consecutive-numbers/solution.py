def all_non_consecutive(arr):
    result = []
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]+1:
            result.append({'i': i, 'n': arr[i]})
    return result