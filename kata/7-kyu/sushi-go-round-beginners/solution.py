def total_bill(s):
    red_plates = s.count('r')
    return (red_plates - red_plates // 5) * 2