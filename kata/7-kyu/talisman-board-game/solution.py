def get_required(player, enemy):
    p = sum(player)
    e = sum(enemy)
    if p == e: return 'Random'
    elif p >= e + 6: return 'Auto-win'
    elif p + 6 <= e: return 'Auto-lose'
    elif p > e: return f'({e + 7 - p}..6)'
    elif p + 5 > e: return f'(1..{p + 5 - e})'
    else: return 'Pray for a tie!'