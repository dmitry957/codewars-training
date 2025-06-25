def all_nines(x):
    if x % 2 == 0 or x % 5 == 0:
        return -1
    
    m = 9
    while m % x != 0:
        m = m * 10 + 9
    return m // x