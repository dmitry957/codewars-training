def DNA_strand(dna):
    complements = { 'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C' }
    return ''.join(map(lambda s: complements.get(s, ''), dna))