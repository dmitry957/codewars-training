def matrix_diagonal(arr, value):
    result = []
    size = len(arr)
    for i in range(size):
        if 0 <= i < size and 0 <= i + value < len(arr[i]):
            result.append(arr[i + value][i])
    return sum(result)