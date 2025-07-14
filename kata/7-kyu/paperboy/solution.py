def cheapest_quote(n):
    total_cost = 0
    prices = [(40, 3.85),
              (20, 1.93),
              (10, 0.97),
              (5, 0.49),
              (1, 0.10)]
    
    for quantity, price in prices:
        count, n = divmod(n, quantity)
        total_cost += count * price

    return round(total_cost, 2)