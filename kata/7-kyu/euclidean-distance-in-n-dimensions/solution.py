from math import sqrt

def euclidean_distance(point1, point2):
    return round(sqrt(sum((a-b)**2 for (a,b) in zip(point1,point2))), 2)