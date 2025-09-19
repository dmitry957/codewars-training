def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"
    products = []
    for i in range(len(num) - 3):
        product = int(num[i]) * int(num[i + 1]) * int(num[i + 2]) * int(num[i + 3])
        products.append(product)
    return min(products)