def well(arr):
    good_ideas = sum(1 for sub in arr for i in sub if isinstance(i, str) and i.lower() == 'good')
    if good_ideas in (1, 2):
        return 'Publish!'
    elif good_ideas > 2:
        return 'I smell a series!'
    else: return 'Fail!'