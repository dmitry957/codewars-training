def cat_mouse(map_, moves):
    map_ = map_.split('\n')
    cat_x, cat_y, mouse_x, mouse_y = -1, -1, -1, -1

    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == 'C':
                cat_x, cat_y = i, j
            elif map_[i][j] == 'm':
                mouse_x, mouse_y = i, j

    if cat_x == -1 or mouse_x == -1:
        return "boring without two animals"

    distance = abs(cat_x - mouse_x) + abs(cat_y - mouse_y)
    return "Caught!" if distance <= moves else "Escaped!"