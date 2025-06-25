def game_winners(gryffindor, slytherin):
    if gryffindor[1] == 'yes': gryffindor[0] += 150
    if slytherin[1] == 'yes': slytherin[0] += 150
    return 'Gryffindor wins!' if gryffindor[0] > slytherin[0] else "Slytherin wins!" if gryffindor[0] < slytherin[0] else 'It\'s a draw!'