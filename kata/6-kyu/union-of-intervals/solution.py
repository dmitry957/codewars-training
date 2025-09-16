def interval_insert(myl: list[tuple[int, int]], interval: tuple[int, int]) -> list[tuple[int, int]]:
    result = []
    i = 0
    n = len(myl)
    while i < n and myl[i][1] < interval[0]:
        result.append(myl[i])
        i += 1

    while i < n and myl[i][0] <= interval[1]:
        interval = (min(interval[0], myl[i][0]), max(interval[1], myl[i][1]))
        i += 1  
    result.append(interval)

    while i < n:
        result.append(myl[i])
        i += 1
    
    return result

