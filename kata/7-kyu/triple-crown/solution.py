def triple_crown(receivers):
    categories = ['Receiving yards', 'Receiving touchdowns', 'Receptions']
    leaders = {category: [] for category in categories}
    
    for category in categories:
        max_val = max(stats[category] for stats in receivers.values())
        for name, stats in receivers.items():
            if stats[category] == max_val:
                leaders[category].append(name)
    
    for name in receivers:
        if all(leaders[cat] == [name] for cat in categories):
            return name
    return 'None of them'