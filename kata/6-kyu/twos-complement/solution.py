def to_twos_complement(binary, bits):
    binary = binary.replace(' ', '')
    if len(binary) != bits:
        raise ValueError('Binary string length must match bits')
    value = int(binary, 2)
    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value
 
def from_twos_complement(n, bits):
    if n >= (1 << (bits - 1)) or n < -(1 << (bits - 1)):
        raise OverflowError(f"Value {n} cannot be represented in {bits} bits")
    if n < 0:
        n = (1 << bits) + n
    return format(n, f'0{bits}b')