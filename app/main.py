import functools
from typing import Callable


def cache_decorator(func: Callable) -> Callable:
    cashh = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in cashh:
            print("Getting from cache")
            return cashh[args]

        print("Calculating new result")
        result = func(*args, **kwargs)

        return result

    return wrapper


@cache_decorator
def add(a: int, b: int) -> int:
    return a + b