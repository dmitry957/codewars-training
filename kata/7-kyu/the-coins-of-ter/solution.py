from math import ceil
def adjust(coin, price):
    return ceil(price / coin) * coin