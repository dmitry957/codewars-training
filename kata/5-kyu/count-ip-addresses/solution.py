def ips_between(start, end):
    start_octets = list(map(int, start.split('.')))
    end_octets = list(map(int, end.split('.')))
    start_decimal = (start_octets[0] * 256**3) + (start_octets[1] * 256**2) + (start_octets[2] * 256**1) + (start_octets[3] * 256**0)
    end_decimal = (end_octets[0] * 256**3) + (end_octets[1] * 256**2) + (end_octets[2] * 256**1) + (end_octets[3] * 256**0)
    return end_decimal - start_decimal