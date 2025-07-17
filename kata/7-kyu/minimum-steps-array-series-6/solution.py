def minimum_steps(numbers, value):
    numbers.sort()
    _sum = 0
    steps = 0
    i = 0
    while _sum < value:
        _sum += numbers[i]
        i += 1
        steps += 1
    return steps - 1