from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args) -> int:
        if cache_dict.get(args) is not None:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        result = func(*args)
        cache_dict[args] = result
        return result

    return inner
