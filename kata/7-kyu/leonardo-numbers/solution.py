def leonardo_numbers(n, L0, L1, add) :
    result = [];
    result.append(L0);
    result.append(L1);
    for i in range(2, n):
        result.append(result[i - 1] + 
                  result[i - 2] + add)
    return result