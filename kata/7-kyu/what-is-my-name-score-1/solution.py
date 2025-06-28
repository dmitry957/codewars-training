alpha = {'ABCDE':1, 'FGHIJ':2, 'KLMNO':3, 'PQRST':4, 'UVWXYZ':5}

def name_score(name):
    total_score = 0
    for char in name:
        total_score += next((score for group, score in alpha.items() if char.upper() in group), 0)
    return { name: total_score }