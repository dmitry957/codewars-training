from functools import reduce

def share_price(invested, changes):
    invested = reduce(lambda acc, v: acc * (1 + v / 100), changes, invested)
    return f"{invested:.2f}"