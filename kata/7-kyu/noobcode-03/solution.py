def letter_check(arr): 
    a, b = arr
    return all(char in a.lower() for char in set(b.lower()))