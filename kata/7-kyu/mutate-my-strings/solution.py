def mutate_my_strings(s1,s2):
    result = []
    length = len(s1)
    index = 0
    while index <= length:
        mutated = s2[:index] + s1[index:]
        index += 1
        result.append(mutated)
    return '\n'.join(list(dict.fromkeys(result))) + '\n'