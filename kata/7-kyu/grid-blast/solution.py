def fire(x, y):
    battlefield = [["top left", "top middle", "top right"],
                    ["middle left", "center", "middle right"],
                    ["bottom left", "bottom middle", "bottom right"]]
    return battlefield[y][x]