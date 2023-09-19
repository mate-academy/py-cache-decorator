from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result: dict = {}

    @wraps(func)
    def inner(*args):
        if args not in result.keys():
            result[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result[args]
    return inner
