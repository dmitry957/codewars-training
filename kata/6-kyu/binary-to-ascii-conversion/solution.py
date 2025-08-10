def binary_to_string(binary):
    bits = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(i, 2)) for i in bits])