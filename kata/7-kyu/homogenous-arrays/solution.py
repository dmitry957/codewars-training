def filter_homogenous(arrays):
    return [inner for inner in arrays if len(inner) and all(isinstance(item, type(inner[0])) for item in inner)]