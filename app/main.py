import functools
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        signature = (func, args)
        if signature in cache_dict:
            result = cache_dict[signature]
            print("Getting from cache")
        else:
            result = func(*args)
            cache_dict[signature] = result
            print("Calculating new result")

        return result

    return wrapper
