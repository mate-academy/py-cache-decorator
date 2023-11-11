from typing import Callable, Any


def cache(func: Callable) -> Callable:
    inner_cache = {}

    def inner(*args) -> Any:

        if args in inner_cache.keys():
            print("Getting from cache")
            return inner_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            inner_cache[args] = result
            return result

    return inner
