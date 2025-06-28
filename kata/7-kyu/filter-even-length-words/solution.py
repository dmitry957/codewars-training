def filter_even_length_words(words):
    return [word for word in filter(lambda x: len(x) % 2 == 0, words)]