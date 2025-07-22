def rake_garden(garden):
    words = garden.lower().split()
    for i, word in enumerate(words):
        if word != 'gravel' and word != 'rock':
            words[i] = 'gravel'
    return ' '.join(words)