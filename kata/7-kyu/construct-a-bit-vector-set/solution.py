def sort_by_bit(seq): 
    bit_vector = 0
    for num in seq:
        bit_vector |= (1 << num)
    return bit_vector