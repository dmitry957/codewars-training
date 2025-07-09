import math
def sctc(sin):
    result = [round(sin, 2)]   
    cos_squared = 1 - sin**2
    if cos_squared < 0:
        cos_squared = 0
    cos = math.sqrt(cos_squared)
    result.append(round(cos, 2))
    
    if cos != 0:
        result.append(round(sin / cos, 2))
    
    if sin != 0:
        result.append(round(cos / sin, 2))
    
    return result