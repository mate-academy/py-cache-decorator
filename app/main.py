from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args) -> int:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict.get(args)

        results = func(*args)
        cache_dict[args] = results
        print("Calculating new result")

        return results

    return wrapper
