def prefix_sums_to_suffix_sums(prefix_sums):
    arr = [prefix_sums[0]]
    for i in range(len(prefix_sums) - 1):
        arr.append(prefix_sums[i + 1] - prefix_sums[i])
    suffix_sums = []
    total = 0
    for x in reversed(arr):
        total += x
        suffix_sums.append(total)
    return suffix_sums[::-1]