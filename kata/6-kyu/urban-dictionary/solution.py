import re

class WordDictionary:
    def __init__(self):
        self._array = []
    
    def add_word(self, word):
        self._array.append(word)

    def search(self, word):
        pattern = "^" + word + "$"
        regex = re.compile(pattern)
        return any(re.fullmatch(regex, w) for w in self._array) 