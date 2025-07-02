def heggeleggleggo(word):
    vowels = 'aeiouAEIOU'
    return ''.join(char + 'egg' if char not in vowels and not char.isspace() else char for char in word)