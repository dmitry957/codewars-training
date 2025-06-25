import collections
def most_frequent_item_count(collection):
    if not len(collection): return 0
    counter = collections.Counter(collection)
    return max(counter.values())