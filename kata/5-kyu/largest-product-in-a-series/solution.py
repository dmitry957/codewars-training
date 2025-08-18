def greatest_product(st):
    max_product = 0
    st = list(map(int, st))
    for i in range(len(st) - 4):
        digits = st[i:i+5]
        product = 1
        for d in digits:
            product *= d
        max_product = max(max_product, product)
    return max_product