def encode(message):
    return gaderypoluki(message)
    
def decode(message):
    return gaderypoluki(message)

import re
def gaderypoluki(message):
    replacements = { 'G': 'A', 'g': 'a', 'a': 'g', 'A': 'G', 'D': 'E', 'd': 'e',
                     'E': 'D', 'e': 'd', 'R': 'Y', 'r': 'y', 'y': 'r', 'Y': 'R',
                     'P': 'O', 'p': 'o', 'o': 'p', 'O': 'P', 'L': 'U', 'l': 'u',
                     'u': 'l', 'U': 'L', 'K': 'I', 'k': 'i', 'i': 'k', 'I': 'K'}
    return re.sub(r'[GADERYPOLUKIgaderypoluki]', lambda x: replacements[x.group()], message)