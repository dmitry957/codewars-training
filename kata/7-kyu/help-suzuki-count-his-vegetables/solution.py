from collections import Counter
def count_vegetables(string):
    vegetables = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]
    filtered = [v for v in filter(lambda x: x in vegetables, string.split())]
    return sorted([(v, k) for k, v in Counter(filtered).items()], key=lambda x: (x[0], x[1]), reverse=True)