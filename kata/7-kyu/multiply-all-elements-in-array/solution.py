from typing import Callable

def multiply_all(arr: list[int]) -> Callable:
    return lambda n: [i * n for i in arr]