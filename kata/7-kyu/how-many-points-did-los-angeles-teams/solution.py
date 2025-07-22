import re
def get_los_angeles_points(results):
    return sum(int(x[1].split(':')[0]) for x in results if bool(re.fullmatch(r'^Los Angeles\s([A-Z][a-z]+)$', x[0])))