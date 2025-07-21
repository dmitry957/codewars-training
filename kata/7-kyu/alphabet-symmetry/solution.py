def solve(strings : list[str]) -> list[int]:
    result = []
    for word in strings:
        count = sum(
            1 for i, ch in enumerate(word.lower())
            if 'a' <= ch <= 'z' and ord(ch) - ord('a') == i
        )
        result.append(count)
    return result