def equable_triangle(a,b,c):
    perimeter = a + b + c
    semi_perimeter = perimeter // 2
    area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5 
    return perimeter == area