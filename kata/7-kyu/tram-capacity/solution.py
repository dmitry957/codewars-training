def tram(stops, descending, onboarding):
    capacity, passengers_count = onboarding[0], onboarding[0]
    for i in range(1, stops):
        passengers_count -= descending[i]
        passengers_count += onboarding[i]
        capacity = max(passengers_count, capacity)
    return capacity