from collections import deque

def number_increasing(n: int) -> bool:
    seen = set()
    q = deque([1])    
    while q:
        x = q.popleft()
        if x == n:
            return True
        if x > n or x in seen:
            continue
        seen.add(x)
        q.append(x * 3)
        q.append(x + 5)
    return False