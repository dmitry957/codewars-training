def generator(_from, _to, _step):
    if _step == 0: return []
    if _from > _to:
        return list(range(_from, _to - 1, -_step))
    return list(range(_from, _to + 1, _step))