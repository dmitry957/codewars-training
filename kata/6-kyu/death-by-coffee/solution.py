def coffee_limits(year, month, day):
    h = int(f'{year:04d}{month:02d}{day:02d}')
    CAFE = 0xCAFE
    DECAF = 0xDECAF
    def find_limit(base, increment):
        val = base
        for i in range(1, 5001):
            val += increment
            if 'DEAD' in hex(val).upper():
                return i
        return 0
    return [find_limit(h, CAFE), find_limit(h, DECAF)]