import re
def solve(s:str) -> int:
    numbers = re.findall(r'\d+', s)
    return max(map(int, numbers))