def max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    return max_profit