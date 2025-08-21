def sort_the_inner_content(words):
    def sort_word(word):
        return word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1]
    words = words.split()
    result = []
    for word in words:
        if len(word) <= 3:
            result.append(word)
        else:
            result.append(sort_word(word))
    return ' '.join(result)