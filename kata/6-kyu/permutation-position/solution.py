def permutation_position(perm):
    result = 0
    for char in perm:
        result = result * 26 + (ord(char) - ord('a'))
    return result + 1
