def sequence_classifier(arr):
    if len(set(arr)) == 1:
        return 5
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return 2 if len(set(sorted_arr)) != len(arr) else 1
    reversed_arr = sorted(arr, reverse=True)
    if arr == reversed_arr:
        return 4 if len(set(reversed_arr)) != len(arr) else 3
    return 0