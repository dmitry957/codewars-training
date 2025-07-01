def arr_adder(arr):
    result = [[] for _ in range(len(arr[0]))]
    for letters in arr:
        for index, letter in enumerate(letters):
                result[index].append(letter)
    return ' '.join([''.join(l) for l in result if len(l)])