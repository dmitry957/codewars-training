def split_the_bill(x):
    average = sum(x.values()) / len(x)
    result = {}
    for key, value in x.items():
        result[key] = round(value - average, 2)
    return result