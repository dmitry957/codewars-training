def correctness(bobs_decisions, expert_decisions): 
    points = 0
    for b, e in zip(bobs_decisions, expert_decisions):
        if b == e: points += 1
        elif b == '?' or e == '?': points += 0.5
    return points