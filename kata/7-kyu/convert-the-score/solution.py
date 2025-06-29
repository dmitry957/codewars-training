def scoreboard(st):
    points = { 'nil': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
    first, second = st.split()[-2:]
    return [points.get(first, 0), points.get(second, 0)]