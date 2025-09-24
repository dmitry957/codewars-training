def split_string(st):
    result = []   
    start_idx = 0
    while start_idx < len(st):
        last_idx = start_idx
        seen = set()
        for i in range(start_idx, len(st)):
            char = st[i]
            last_idx = max(last_idx, st.rfind(char))
            seen.add(char)
            if i == last_idx:
                result.append(last_idx - start_idx + 1)
                start_idx = i + 1
                break
    return result