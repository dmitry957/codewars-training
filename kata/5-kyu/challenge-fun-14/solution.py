def target_game(values):
    if not values:
        return 0
    if len(values) == 1:
        return max(values[0], 0)
    
    prev2 = 0
    prev1 = max(values[0], 0)
    
    for i in range(1, len(values)):
        current = max(prev2 + max(values[i], 0), prev1)
        prev2 = prev1
        prev1 = current
    return prev1