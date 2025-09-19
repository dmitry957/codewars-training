def up_array(arr):
    if not len(arr) or any(i < 0 or i > 9 for i in arr):
        return None
    
    result = arr[:]
    carry = 1

    for i in range(len(result) - 1, -1, -1):
        if carry == 0:
            break
        result[i] += carry
        if result[i] > 9:
            result[i] = 0
            carry = 1
        else:
            carry = 0

    if carry:
        result = [1] + result

    return result