def kangaroo(kanga1, rate1, kanga2, rate2):
    if rate1 == rate2:
        return kanga1 == kanga2
    if (kanga2 - kanga1) % (rate1 - rate2) == 0 and (kanga2 - kanga1) // (rate1 - rate2) >= 0:
        return True
    return False