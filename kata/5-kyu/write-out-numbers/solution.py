def number2words(n):
    representation = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    def get_words_under_100(number):
        if number < 20:
            return representation[number]
        tens, below = divmod(number, 10)
        if below == 0:
            return representation[tens * 10]
        return representation[tens * 10] + '-' + representation[below]
    
    def get_words_under_1000(number):
        if number < 100:
            return get_words_under_100(number)
        hundreds, below = divmod(number, 100)
        if below == 0:
            return representation[hundreds] + ' hundred'
        return representation[hundreds] + ' hundred ' + get_words_under_100(below)
    
    if n < 100:
        return get_words_under_100(n)
    
    if n < 1000:
        return get_words_under_1000(n)
    
    thousands, below = divmod(n, 1000)
    result = get_words_under_1000(thousands) + ' thousand'
    if below != 0:
        if below < 100:
            result += ' ' + get_words_under_100(below)
        else:
            result += ' ' + get_words_under_1000(below)
    return result