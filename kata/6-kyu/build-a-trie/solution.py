def build_trie(*words: list[str]) -> dict:
    trie = {}
    for word in words:
        node = trie
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if prefix not in node:
                node[prefix] = None
            if node[prefix] is None and i != len(word):
                node[prefix] = {}
            node = node[prefix] if node[prefix] is not None else {}
    return trie