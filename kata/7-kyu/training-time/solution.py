def shuffle_it(*args):
    arr = args[0]
    for i in range(1, len(args)):
        first, second = args[i]
        arr[first], arr[second] = arr[second], arr[first]
    return arr