def find_in_array(seq, predicate):
    index = 0
    while index <= len(seq) - 1:
        if predicate(seq[index], index):
            return index
        index += 1
    return -1