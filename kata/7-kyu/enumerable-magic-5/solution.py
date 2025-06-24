def one(xs, f):
    return sum(1 for item in xs if f(item)) == 1