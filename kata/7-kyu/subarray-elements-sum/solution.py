def elements_sum(arr, d = 0):
    sum_ = 0
    position = len(arr) 
    for i, subarray in enumerate(arr):
        try:
            val = subarray[position - 1 - i]
            sum_ += 0 if val == 0 else val
        except (IndexError, TypeError):
            sum_ += d
    return sum_