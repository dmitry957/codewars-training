def histogram(results):
    result = []
    total = sum(results)
    for i, p in enumerate(results):
        percent = 0 if total == 0 else (p * 100) // total
        bar = '\u2588' * (50 * percent // 100)
        line = f'{i + 1}|{bar}'
        if percent > 0:
            line += f' {percent}%'
        result.append(line)
    return '\n'.join(list(reversed(result))) + '\n'