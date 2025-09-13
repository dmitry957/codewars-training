def solve(s, idx):
    if idx < 0 or idx >= len(s) or st[idx] != '(':
        return -1
    
    count = 1
    for i in range(idx + 1, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                return i
    return -1