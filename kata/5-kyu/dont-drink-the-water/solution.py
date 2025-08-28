def separate_liquids(glass):
    liquid_densities = { 'H': 1.36, 'W': 1, 'A': 0.87, 'O': 0.8 }
    if not len(glass):
        return []
    rows = len(glass)
    cols = len(glass[0])
    flattened = [cell for row in glass for cell in row]
    flattened.sort(key=lambda d: liquid_densities[d])
    result = [
        flattened[i*cols:(i+1)*cols]
        for i in range(rows)
    ]
    return result