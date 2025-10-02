from functools import reduce
def max_sequence(arr):
    return reduce(lambda acc, x: (max(acc[0] + x, 0), max(acc[1], max(acc[0] + x, 0))), arr, (0, 0))[1]