words = []

def haiku_wizard(arr):
    haiku = []
    for line in arr:
        translated = []
        for syllable in line:
            syllable_number, member = list(map(int, str(syllable)))
            translated.append(words[syllable_number - 1][member])
        haiku.append(' '.join(translated))
    return '\n'.join(haiku)