def num_tiles(width,height):
    if width == 0 or height == 0:
        return 0
    size = 1 << (min(width, height).bit_length() - 1)
    tiles_wide = width // size
    tiles_height = height // size
    tiles = tiles_wide * tiles_height
    
    remainder_right = num_tiles(width % size, height)
    remainder_bottom = num_tiles(size * tiles_wide, height % size)
    return tiles + remainder_right + remainder_bottom