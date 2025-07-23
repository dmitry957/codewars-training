def numbers_grouping(a):
    return len(set((num - 1) // 10**4 for num in a)) + len(a)