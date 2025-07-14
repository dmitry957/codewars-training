def noonerize(numbers):
    if not all(isinstance(num, int) and num >= 0 for num in numbers):
        return 'invalid array'
    a, b = map(str, numbers)
    
    if not a or not b:
        return 'invalid array'
    
    swapped_a = b[0] + a[1:] if len(a) > 1 else b[0]
    swapped_b = a[0] + b[1:] if len(b) > 1 else a[0]
    
    result = abs(int(swapped_a) - int(swapped_b))
    return result
