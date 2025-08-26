def find_uniq(arr):
    def normalize(s):
        return ''.join(sorted(set(s.lower().replace(' ', ''))))
    freq = {}
    normalized = []
    for s in arr:
        n = normalize(s)
        normalized.append(n)
        freq[n] = freq.get(n, 0) + 1
    for n in normalized:
        if freq[n] == 1:
            return arr[normalized.index(n)]