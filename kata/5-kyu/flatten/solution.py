def flatten(*args) -> list:
    result = []
    for item in args:
        if isinstance(item, list):
            result.extend(flatten(*item))
        else:
            result.append(item)
    return result