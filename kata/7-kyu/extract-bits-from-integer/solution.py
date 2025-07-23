def extract_bits(field: int, offset: int, length: int):
    field &= (1 << 64) - 1
    if offset >= 64:
        return 0
    if offset + length > 64:
        length = 64 - offset

    return (field >> offset) & ((1 << length) - 1)