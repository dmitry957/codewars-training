def max_multiple(divisor, bound):
    while bound % divisor != 0:
        bound -= 1
    return bound