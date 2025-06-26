def burner(c,h,o):
    water = min(h // 2, o)
    h -= water * 2
    o -= water

    carbon_dioxide = min(c, o // 2)
    c -= carbon_dioxide
    o -= carbon_dioxide * 2

    methane = min(c, h // 4)
    return (water, carbon_dioxide, methane)