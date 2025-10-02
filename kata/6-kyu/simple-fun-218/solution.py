def replace_words(sentence):
    words = sentence.split()
    n = len(words)
    sorted_words = sorted(enumerate(words), key=lambda x: len(x[1]))
    result = words[:]
    for i in range(n // 2):
        short_idx, _ = sorted_words[i]
        long_idx, _ = sorted_words[-(i + 1)]
        result[short_idx], result[long_idx] = result[long_idx], result[short_idx]

    for i, word in enumerate(result):
        if i == 0:
            result[i] = word.capitalize()
        else:
            result[i] = word if word == 'I' else word.upper() if word == 'i' else word.lower()
    return ' '.join(result)