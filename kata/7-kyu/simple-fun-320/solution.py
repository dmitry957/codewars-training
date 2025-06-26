def scratch(lottery):
    total = 0
    for l in lottery:
        characters = set(l.split())
        if len(characters) == 2:
            bonus = sorted(characters)[0] 
            total += int(bonus)
    return total