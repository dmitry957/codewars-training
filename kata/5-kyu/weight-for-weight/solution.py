def order_weight(strng):
    if not strng:
        return ''    
    num_weights = [(num, sum(int(d) for d in num)) for num in strng.split()]
    num_weights.sort(key=lambda x: (x[1], x[0]))
    result = [x[0] for x in num_weights]
    return ' '.join(result)