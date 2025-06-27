def sort_by_binary_ones(numList):
    return sorted(numList, key=lambda i: (-bin(i).count('1'), len(bin(i)[2:]) i))