def seven_wonders_science(compasses, gears, tablets):
    glyph_amount = compasses**2 + gears**2 + tablets**2
    if compasses == 0 or gears == 0 or tablets == 0: return glyph_amount
    distinct_set = 7 * min(compasses, gears, tablets)
    return distinct_set + glyph_amount