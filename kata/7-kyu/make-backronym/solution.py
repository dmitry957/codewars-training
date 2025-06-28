#preloaded variable: "dictionary"

def make_backronym(acronym):
    words = []
    for char in acronym:
        words.append(dictionary.get(char.upper(), ''))
    return ' '.join(words)