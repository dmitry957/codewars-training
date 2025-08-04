def make_looper(string: str) -> callable:
    iterator = CyclicIterator(string)
    return lambda: next(iterator)

class CyclicIterator:
    def __init__(self, string: str):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.string:
            raise StopIteration
        char = self.string[self.index]
        self.index = (self.index + 1) % len(self.string)
        return char