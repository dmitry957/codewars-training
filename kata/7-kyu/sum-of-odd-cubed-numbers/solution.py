def cube_odd(arr):
    if not all(type(i) == int for i in arr):
        return None
    return sum(i**3 for i in arr if i**3 % 2 != 0)