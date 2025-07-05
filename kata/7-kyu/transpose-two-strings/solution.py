def transpose_two_strings(arr):
    first_word, second_word = arr
    result = []
    max_len = max(len(first_word), len(second_word))
    first_word = first_word.ljust(max_len)
    second_word = second_word.ljust(max_len)
    for a, b in zip(first_word, second_word):
        result.append(f'{a} {b}')
    return '\n'.join(result)