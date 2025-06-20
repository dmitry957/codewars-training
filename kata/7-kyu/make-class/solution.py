def make_class(*args):
    class Dynamic:
        def _init__(self, *values):
            for i, prop in enumerate(args):
                setattr(self, prop, values[i] if i < len(values) else None)
    return Dynamic