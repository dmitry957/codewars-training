def sep_str(st):
    if not st:
        return []
    words = st.split()
    max_len = max(map(len, words))
    return [[w[i] if i < len(w) else '' for w in words] for i in range(max_len)]
