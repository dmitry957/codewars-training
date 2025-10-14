def avg_array(arrs):
    return [sum(col) / len(col) for col in zip(*arrs)]