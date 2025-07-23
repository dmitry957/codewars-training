def add(*args):
    return sum((index + 1)*value for index, value in enumerate(args))