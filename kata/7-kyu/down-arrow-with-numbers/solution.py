def get_a_down_arrow_of(n):
    if n < 1:
        return ""
    
    lines = []
    for i in range(n):
        indent = ' ' * i
        peak = n - i
        ascending = ''.join(str(j % 10) for j in range(1, peak + 1))
        descending = ''.join(str(j % 10) for j in range(peak - 1, 0, -1))
        line = indent + ascending + descending
        lines.append(line)
    
    return '\n'.join(lines)