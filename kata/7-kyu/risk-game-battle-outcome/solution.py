def battle_outcome(attacker, defender):
    attacker_units_lost = 0
    defender_units_lost = 0
    for a, d in zip(sorted(attacker)[::-1], sorted(defender)[::-1]):
        if a > d:
            defender_units_lost += 1
        elif a <= d:
            attacker_units_lost += 1
    return (attacker_units_lost, defender_units_lost)