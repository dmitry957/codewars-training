def solve(a):
    even_count = sum(1 for i in a if type(i) == int and i % 2 == 0)
    odd_count = sum(1 for i in a if type(i) == int and i % 2 != 0)
    return even_count - odd_count