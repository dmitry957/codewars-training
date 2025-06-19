def alphabet_war(fight):
    left_side = { 'w': 4, 'p': 3, 'b': 2, 's': 1 }
    right_side = { 'm': 4, 'q': 3, 'd': 2, 'z': 1 }
    left_sum = 0
    right_sum = 0
    for char in fight:
        left_sum += left_side.get(char, 0)
        right_sum += right_side.get(char, 0)
    return 'Right side wins!' if right_sum > left_sum else 'Left side wins!' if left_sum > right_sum else "Let's fight again!"