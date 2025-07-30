def find_function(func, arr):
    f = next((item for item in func if callable(item)), None)
    return [*filter(f, arr)] if f else []