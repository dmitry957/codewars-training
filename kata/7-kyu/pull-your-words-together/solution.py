def sentencify(words):
    if len(words) == 1:
        return words[0].capitalize() + '.'
    return f"{words[0] if words[0].isupper() else words[0].capitalize()} {' '.join(words[1:len(words) - 1])} {words[-1]}."