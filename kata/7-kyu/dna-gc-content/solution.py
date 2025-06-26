def gc_content(seq):
    return seq.count('G') + seq.count('C') / len(seq) * 100 if len(seq) else 0.0