def tribonacci(signature, n):
    if n == 0:
        return []
    
    result = signature[:n]
    if n > 3:
        for _ in range(n - 3):
            next_num = result[-1] + result[-2] + result[-3]
            result.append(next_num)
    return result