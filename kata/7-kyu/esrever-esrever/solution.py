def esrever(st):
    words = st.split()
    if not words:
        return ''
    
    *middle, last = words
    punctuation = last[-1] if not last[-1].isalnum() else ''
    last_word = last[:-1] if punctuation else last
    reversed_words = [word[::-1] for word in middle + [last_word]]
    return ' '.join(reversed(reversed_words)) + punctuation