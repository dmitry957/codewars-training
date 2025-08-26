from math import gcd
from functools import reduce

def solution(lst):
    _gcd = reduce(gcd, lst)
    return _gcd * len(lst)