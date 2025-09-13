def vowel_shift(text,n):
    if not text:
        return text
    vowels = 'aeiouAEIOU'
    indices = [i for i, char in enumerate(text) if char in vowels]
    if not indices:
        return text
    vowel_chars = [text[i] for i in indices]
    n = n % len(vowel_chars)
    shifted = vowel_chars[-n:] + vowel_chars[:-n]
    text_list = list(text)
    for i, char in zip(indices, shifted):
        text_list[i] = char
    return ''.join(text_list)