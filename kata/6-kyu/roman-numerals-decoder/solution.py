def solution(roman : str) -> int:
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result, previous = 0, 0
    for char in roman[::-1]:
        value = numerals[char]
        if value < previous:
            result -= value
        else:
            result += value
        previous = value
    return result