def vaporcode(s):
    return '  '.join([char.upper() for char in s.replace(' ', '')])