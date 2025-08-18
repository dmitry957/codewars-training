def closest(strng):
    if not strng:
        return []
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))
    numbers = strng.split()
    weights = [[sum_of_digits(num), index, int(num)] for index, num in enumerate(numbers)]
    weights.sort(key=lambda x: (x[0], x[1]))
    min_diff = float('inf')
    result = []
    for i in range(len(weights) - 1):
        diff = abs(weights[i][0] - weights[i + 1][0])
        if diff < min_diff:
            min_diff = diff
            result = [weights[i], weights[i + 1]]
    return result