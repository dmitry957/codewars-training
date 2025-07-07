def sc(apple):
    return next(((i, j) for i, row in enumerate(apple) for j, val in enumerate(row) if val == 'B'))