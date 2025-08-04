from math import sin, pi
def area_of_inscribed_polygon(circle_radius, number_of_sides):
    return (number_of_sides * circle_radius ** 2) / 2 * sin(2 * pi / number_of_sides)