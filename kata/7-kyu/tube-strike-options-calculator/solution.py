def calculator(distance, bus_drive, bus_walk):
    walk = 5
    bus = 8
    walk_time = distance / walk * 60
    bus_time = ((bus_drive / bus) + (bus_walk / walk)) * 60
    if walk_time > 120:
        return 'Bus'
    if walk_time < 10:
        return 'Walk'
    
    if walk_time < bus_time:
        return 'Walk'
    elif bus_time < walk_time:
        return 'Bus'
    else:
        return 'Walk'