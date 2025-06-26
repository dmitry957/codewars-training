def any_odd(x):
    bin_num = reversed(bin(x)[2:])
    return any(bit == '1' and i % 2 != 0 for i, bit in enumerate(bin_num))