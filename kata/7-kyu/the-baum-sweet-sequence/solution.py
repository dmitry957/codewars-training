def baum_sweet():
    n = 0
    while True:
        if n == 0:
            yield 1
        else:
            binary = bin(n)[2:]
            zero_blocks = binary.split('1')
            if any(len(block) % 2 == 1 for block in zero_blocks if block != ''):
                yield 0
            else:
                yield 1
        n += 1