def binary_to_string(binary):
    parts = binary.split('0b')
    chars = []
    for p in parts:
        if p:
            chars.append(chr(int(p, 2)))
    return ''.join(chars)