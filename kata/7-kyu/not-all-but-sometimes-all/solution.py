def remove(text, what):
    for key, value in what.items():
        text = text.replace(key, '', value)
    return text