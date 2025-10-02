def count_feelings(st, arr):
    result = []
    for word in arr:
        if all(char in st and word.count(char) <= st.count(char) for char in word):
            result.append(word)
    
    count = len(set(result))    
    return f"{count} feeling{'s' if count != 1 else ''}."