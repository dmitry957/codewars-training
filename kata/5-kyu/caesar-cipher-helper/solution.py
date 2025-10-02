import string
class CaesarCipher(object):
    _alphabet = string.ascii_lowercase
    
    def __init__(self, shift):
        self.shift = shift % 26

    def encode(self, st):
        result = []
        for ch in st:
            if ch.lower() in self._alphabet:
                idx = self._alphabet.index(ch.lower())
                new_char = self._alphabet[(idx + self.shift) % 26]
                result.append(new_char.upper() if ch.isupper() else new_char)
            else:
                result.append(ch)
        return ''.join(result).upper()
        
    def decode(self, st):
        result = []
        for ch in st:
            if ch.lower() in self._alphabet:
                idx = self._alphabet.index(ch.lower())
                new_char = self._alphabet[(idx - self.shift) % 26]
                result.append(new_char.upper() if ch.isupper() else new_char)
            else:
                result.append(ch)
        return ''.join(result)