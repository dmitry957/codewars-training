from collections import Counter

def duplicate_count(text):
    text_count = Counter(text.lower())
    return sum(1 for count in text_count.values() if count > 1)