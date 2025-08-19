def simple_fizz_buzz(i, fizz='Fizz', buzz='Buzz', three=3, five=5):
    result = ''
    if i % three == 0:
        result += fizz
    if i % five == 0:
        result += buzz
    return result or i

def fizz_buzz_custom(*args):
    if len(args) not in (0, 2, 4):
        raise TypeError('fizz_buzz_custom() takes 0, 2 or 4 positional arguments')
    if len(args) == 0:
        return [simple_fizz_buzz(i) for i in range(1, 101)]
    elif len(args) == 2:
        foo, bar = args
        return [simple_fizz_buzz(i, foo, bar) for i in range(1, 101)]
    else:
        foo, bar, three, five = args
        return [simple_fizz_buzz(i, foo, bar, three, five) for i in range(1, 101)]