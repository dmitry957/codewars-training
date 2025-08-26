def maximize_earnings(earnings, k):
    n = len(earnings)
    if n == 0:
        return 0
    neg_inf = float('-inf')
    dp_break = 0
    dp_work = [neg_inf] * (k + 1)
    for v in earnings:
        new_work = [neg_inf] * (k + 1)
        new_break = max([dp_break] + dp_work[1:])
        new_work[1] = dp_break + v
        for j in range(2, k + 1):
            if dp_work[j - 1] != neg_inf:
                new_work[j] = dp_work[j - 1] + v
        dp_break, dp_work = new_break, new_work
        
    return int(max(dp_break, max(dp_work[1:]))) 