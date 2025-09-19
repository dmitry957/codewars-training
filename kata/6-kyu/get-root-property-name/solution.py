def get_root_property(dict_, value):
    for k, v in dict_.items():
        if isinstance(v, list) and value in v:
            return k
        elif isinstance(v, dict):
            result = get_root_property(v, value)
            if result:
                return k
    return None