def magic_sum(arr):
    return sum(i for i in arr if i % 2 != 0 and '3' in str(i))