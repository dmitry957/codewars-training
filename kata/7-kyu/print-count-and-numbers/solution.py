import re
def count_me(data):
    if not data or not re.fullmatch(r'\d+', data): return ''
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(f'{count}{data[i - 1]}')
            count = 1
    result.append(f'{count}{data[-1]}')
    return ''.join(result)