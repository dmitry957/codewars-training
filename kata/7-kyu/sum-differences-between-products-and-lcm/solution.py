def sum_differences_between_products_and_LCMs(pairs):
    return sum(x[0] * x[1] - lcm(x[0], x[1]) if x[1] > 0 else 0 for x in pairs)

def gcd(x, y):
    while y:      
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x, y)