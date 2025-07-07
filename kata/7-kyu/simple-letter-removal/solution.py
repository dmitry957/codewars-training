def solve(st,k): 
    st = list(st)
    for letter in map(chr, range(ord('a'), ord('z') + 1)):
        if k == 0:
            break
        i = 0
        while i < len(st) and k > 0:
            if st[i] == letter:
                st.pop(i)
                k -= 1
            else:
                i += 1
    return ''.join(st)