from math import gcd

def gcd_matrix(a,b):
    total = 0
    count = 0
    for y in b:
        for x in a:
            total += gcd(x, y)
            count += 1
    
    return round(total / count, 3)