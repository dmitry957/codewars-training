def skiponacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    fib = fib[:n]
    result = [str(num) if i % 2 == 0 else 'skip' for i, num in enumerate(fib)]
    return ' '.join(result)