def direction(facing, turn):
    directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    return directions[(directions.index(facing) + turn // 45) % len(directions)]