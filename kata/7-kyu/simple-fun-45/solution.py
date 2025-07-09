import string
def new_numeral_system(number):
    letters = string.ascii_uppercase
    number_index = letters.index(number)
    result = []
    for i in range(number_index + 1):
        for j in range(number_index + 1):
            if i + j == number_index and j >= i:
                result.append(f'{letters[i]} + {letters[j]}')
    return result