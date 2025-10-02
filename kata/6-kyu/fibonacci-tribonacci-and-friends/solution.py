def xbonacci(signature, n):
    result = signature[:n]
    for i in range(n - len(signature)):
        result.append(sum(result[-len(signature):]))
    return result