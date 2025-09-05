from functools import reduce
def select_subarray(arr):
    quotients = {}
    index = 0
    while index != len(arr):
        subarr = arr[:index] + arr[index + 1:]
        sub_product = reduce(lambda a, b: a * b, subarr)      
        sub_sum = sum(subarr)
        if sub_sum != 0:
            quotients[index] = abs(sub_product // sub_sum)
        index += 1
    min_quotient = min(quotients.values())
    indicies = [k for k, v in quotients.items() if v == min_quotient]
    result = []
    for i in indicies:
        result.append([i, arr[i]])
    return result[0] if len(result) == 1 else result