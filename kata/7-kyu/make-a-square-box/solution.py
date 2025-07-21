def box(n):
    result = ["-" * n]
    for i in range(n - 2):
        result.append("-" + (" " * (n - 2)) + "-")
    result.append("-" * n)
    return result