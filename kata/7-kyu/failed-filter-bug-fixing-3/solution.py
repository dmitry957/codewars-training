def filter_numbers(string):
    return ''.join(x for x in string if x.isalpha() or x.isspace())