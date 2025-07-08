from math import inf
def sum_two_smallest_numbers(numbers):
    smallest = inf
    second = inf
    
    for num in numbers:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second:
            second = num
    return smallest + second