from typing import List, Tuple
from collections import deque

def word_problem(rules: List[Tuple[str, str]], from_str: str, to_str: str, applications: int) -> bool:
    queue = deque([(from_str, 0)])
    visited = set([from_str])
    while queue:
        s, steps = queue.popleft()
        if s == to_str:
            return True
        if steps >= applications:
            continue
        for lhs, rhs in rules:
            start = 0
            while True:
                index = s.find(lhs, start)
                if index == -1:
                    break
                new_s = s[:index] + rhs + s[index + len(lhs):]
                if new_s not in visited:
                    visited.add(new_s)
                    queue.append((new_s, steps + 1))
                start = index + 1
    return False