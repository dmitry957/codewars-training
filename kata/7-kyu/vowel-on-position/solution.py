def check_vowel(strng, position):
    return 0 <= position < len(strng) and strng[position] in 'aeiouAEIOU'