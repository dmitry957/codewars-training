MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-..': 'D' '''etc.'''}

def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    result = []
    for word in words:
        characters = word.split()
        decoded_word = []
        for char in characters:
            decoded_word.append(MORSE_CODE.get(char, char))
        result.append(''.join(decoded_word))
    return ' '.join(result)