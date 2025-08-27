def even_odd(arr):
    total = 0
    for i, num in enumerate(arr):
        if i % 2 == 0:
            total += num
        else:
            total *= num
            
    return total