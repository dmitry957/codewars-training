def shortest_to_char(s, c):
    if not s or not c or c not in s:
        return []
    
    length = len(s)
    result = [float('inf')] * length
    prev = float('-inf')
    
    for i in range(length):
        if s[i] == c:
            prev = i
        result[i] = i - prev
    
    prev = float('inf')
    for i in reversed(range(length)):
        if s[i] == c:
            prev = i
        result[i] = min(result[i], prev - i)
    
    return result