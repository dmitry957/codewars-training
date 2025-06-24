def pattern(n):
    result = []
    digit_count = n
    current_digit = 1
    for i in range(1, n + 1):
        row = ' ' * i + ' '.join([str(current_digit)] * digit_count)
        result.append(row)
        digit_count -= 1
        current_digit = current_digit + 1 if current_digit < 9 else 0
    return '\n'.join(result)