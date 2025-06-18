def convert_bits(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    if a < b:
        bin_a = bin_a.zfill(len(bin_b))
    elif a > b:
        bin_b = bin_b.zfill(len(bin_a))
    mismatches = sum(c1 != c2 for c1, c2 in zip(bin_a, bin_b))
    return mismatches