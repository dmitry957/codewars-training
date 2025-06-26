def mirror(data: list) -> list:
    sorted_data = sorted(data)
    return sorted_data + sorted_data[::-1][1:]