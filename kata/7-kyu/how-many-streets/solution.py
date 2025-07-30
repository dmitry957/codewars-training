def count_streets(streets, drivers):
    street_index = {street: i for i, street in enumerate(streets)}
    return [abs(street_index[a] - street_index[b]) - 1 for a, b in drivers]