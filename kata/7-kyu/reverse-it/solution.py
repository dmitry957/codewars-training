def reverse_it(data):
    if isinstance(data, (int, float, str)):
        reversed_str = str(data)[::-1]
        return type(data)(reversed_str)
    return data