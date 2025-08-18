# -*- coding: utf-8 -*-
def dative(word):
    reversed_word = word[::-1]
    for letter in reversed_word:
        if letter in ('e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'):
            return word + 'nek'
        if letter in ('a', 'á', 'o', 'ó', 'u', 'ú'):
            return word + 'nak'
    return word