import math
def log(real, imag):
    r = math.hypot(real, imag)
    if r == 0.0:
        return None
    real_ = math.log(r)
    imag_ = math.atan2(imag, real)
    return [real_, imag_]