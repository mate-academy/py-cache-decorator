from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    @wraps(func)
    def inner(*args) -> Any:

        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        print("Calculating new result")
        result = func(*args)
        cache_dict[args] = result
        return result

    return inner
