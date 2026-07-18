import functools
from typing import Callable

def cache(func: Callable) -> Callable:
    cashh = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in cashh:
            print("Getting from cache")
            return cashh[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cashh[args] = result
        return result

    return wrapper


@cache
def add(a: int, b: int) -> int:
    return a + b
