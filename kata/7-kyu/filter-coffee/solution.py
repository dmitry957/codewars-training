def search(budget, prices):
    return ','.join(map(str, sorted([p for p in prices if p <= budget])))