def describe_the_shape(angles):
    if angles <= 2:
        return "this will be a line segment or a dot"
    return f"This shape has {angles} sides and each angle measures {((angles-2) * 180)//angles}"