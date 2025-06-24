from math import log
def largest_power(N):
    return max(0, int(log(N, 3))) - (3 ** int(log(N, 3)) >= N)