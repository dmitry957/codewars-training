def how_much_coffee(events):
    count = 0
    for event in events:
        if event in ('CW', 'DOG', 'CAT', 'MOVIE'):
            count += 2
        if event in ('cw', 'dog', 'cat', 'movie'):
            count += 1
    return count if count <= 3 else 'You need extra sleep'