import re
def find_missing_number(sequence):
    if not sequence: return 0
    elements = sequence.split()
    pattern = r'^(0|[1-9]\d*)$'
    if not all(re.match(pattern, element) for element in elements):
         return 1
    else:
        integers = sorted(map(int, elements))
        max_num = integers[-1]
        expected = set(range(1, max_num + 1))
        actual = set(integers)
        missing = expected - actual
        if not missing:
            return 0
        return min(missing)