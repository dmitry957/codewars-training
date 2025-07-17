from collections import Counter
def count_duplicates(name,age,height):
    entries = list(zip(name, age, height))
    counts = Counter(entries)
    return sum(count - 1 for count in counts.values() if count > 1)