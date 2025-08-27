def getfib():
    a, b = 0, 1
    def fib():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result
    return fib

def genfib_iter():
    def wrapper():
        yield from _genfib()

    def _genfib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    gen = wrapper()

    def fib():
        return next(gen)
    
    return fib