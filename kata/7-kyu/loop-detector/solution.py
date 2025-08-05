def has_loop(arr: list[int]) -> bool:
    index = 0
    already_visited = []
    while index not in already_visited:
        if index >= len(arr):
            return False
        already_visited.append(index)
        index = arr[index]
    return True