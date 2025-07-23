def censor(sentence):
    words = sentence.split()
    result = []
    pancakes = ['pancakes', 'flapjacks', 'slapjacks', 'hotcakes']
    waffles = ['waffles', 'crepes', 'blintzes']
    highlight_or_censor = ['syrup', 'honey', 'jam', 'butter', 'chocolate', 'margarine']
    has_waffles = any(item in words for item in waffles)
    for word in words:
        if word.lower() in pancakes or (not has_waffles and word.lower() in highlight_or_censor):
            result.append('*' * len(word))
        elif word.lower() in waffles or (has_waffles and word.lower() in highlight_or_censor):
            result.append(f'**{word}**')
        else:
            result.append(word)
    return ' '.join(result)