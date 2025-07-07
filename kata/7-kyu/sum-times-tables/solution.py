def sum_times_tables(table, a, b):
    return sum(j * i for i in range(a, b + 1) for j in table)