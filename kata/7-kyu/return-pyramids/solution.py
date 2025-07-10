def pyramid(n):
    result = []
    left_spaces = n - 1
    inner_spaces = 0
    for i in range(n - 1):     
        floor = ' ' * left_spaces + '/' + ' ' * inner_spaces + '\\'  
        left_spaces -= 1
        inner_spaces += 2
        result.append(floor)
    result.append(' ' * left_spaces + '/' + '_' * inner_spaces + '\\')
    return '\n'.join(result) + '\n'