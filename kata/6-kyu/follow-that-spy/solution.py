def find_routes(routes):
    destinations = {dest for _, dest in routes}
    start = next(origin for origin, _ in routes if origin not in destinations)
    route_map = {origin: dest for origin, dest in routes}
    result = [start]
    while start in route_map:
        start = route_map[start]
        result.append(start)
    return ', '.join(result)