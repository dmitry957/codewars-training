def find_nth_occurrence(substring, string, occurrence=1):
    index = -1
    for _ in range(occurrence):
        index = string.find(substring, index + 1)
        if index == -1:
            return -1
    return index

import re
def find_nth_occurrence_re(substring, string, occurrence=1):
    if not substring or occurrence < 1:
        return -1

    pattern = f'(?={re.escape(substring)})'
    matches = [m.start() for m in re.finditer(pattern, string)]
    if len(matches) < occurrence:
        return -1
    return matches[occurrence - 1]