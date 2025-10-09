def de_nico(key, msg):
    sorted_key = sorted(list(key))
    numeric_key = [sorted_key.index(ch) + 1 + sum(1 for i, c in enumerate(key[:idx]) if c == ch)
                   for idx, ch in enumerate(key)]
    
    klen = len(key)
    rows = [list(msg[i:i+klen]) for i in range(0, len(msg), klen)]    
    decoded_rows = []
    for row in rows:
        row += [''] * (klen - len(row))
        reordered = [''] * klen
        for i, pos in enumerate(numeric_key):
            reordered[i] = row[pos-1]
        decoded_rows.append(''.join(reordered))
    return ''.join(decoded_rows).rstrip()