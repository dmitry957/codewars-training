def days_of(items):
    n = len(items)
    result = []
    for i, item in enumerate(items):
        count = (n - i) * (i + 1)
        result.append(f"{count} {item}") 
    return result