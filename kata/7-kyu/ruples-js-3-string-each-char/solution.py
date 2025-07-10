import types
def each_char(string, arg):
    if isinstance(arg, types.FunctionType):
        return ''.join([arg(char) for char in string])
    if isinstance(arg, str):
        return ''.join([char + arg for char in string])