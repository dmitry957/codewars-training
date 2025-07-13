def pillow(s):
    pillows = set([i for i, char in enumerate(s[0]) if char == 'n'])
    fridges = set([i for i, char in enumerate(s[1]) if char == 'B'])
    return len(pillows & fridges) > 0