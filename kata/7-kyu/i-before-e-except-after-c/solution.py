import re
def i_before_e(s):
    def fix(match):
        seq = match.group()
        before = match.start() - 1
        preceding = s[before] if before >= 0 else ''
        i_count = seq.count('i')
        e_count = seq.count('e')
        if preceding == 'c':
            return 'e' * e_count + 'i' * i_count
        else:
            return 'i' * i_count + 'e' * e_count

    return re.sub(r'[ie]+', fix, s)