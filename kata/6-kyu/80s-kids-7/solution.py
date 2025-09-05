class Robot:
    
    def __init__(self):
        self._data = set(['i', 'do', 'input', 'not', 'already', 'know', 'the', 'word','thank', 'you', 'for','me','teaching','understand'])
        
    def learn_word(self, word):
        if not word.isalpha():
            return 'I do not understand the input'
        normalized = word.lower()
        if normalized in self._data:
            return f'I already know the word {word}'
        else:
            self._data.add(normalized)
            return f'Thank you for teaching me {word}'