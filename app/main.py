from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    # count = 0
    result_cache = dict()

    @wraps(func)
    def inner(*args) -> None:
        item_func = args
        if item_func in result_cache:
            print("Getting from cache")
            return result_cache[item_func]
        else:
            print("Calculating new result")
            result = func(*args)
            result_cache[item_func] = result
            return result
    return inner
