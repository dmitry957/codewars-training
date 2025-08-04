def closure(base_set, limit=None):
    result = {1}
    frontier = [1]
    while frontier:
        current = frontier.pop()
        for b in base_set:
            new_val = current * b
            if limit and new_val > limit:
                continue
            if new_val not in result:
                result.add(new_val)
                frontier.append(new_val)
    return result

def smallest_set_with_same_closure(s):
    s = sorted(set(s))
    minimal = set()
    max_element = max(s) if len(s) else 0
    for x in s:
        if x not in closure(minimal, limit=max_element):
            minimal.add(x)
    return minimal