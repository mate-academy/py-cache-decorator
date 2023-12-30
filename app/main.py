from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_values = {}

    def inner(*args) -> Any:
        if args in cache_values:
            print("Getting from cache")
            return cache_values[args]
        else:
            print("Calculating new result")
            result = func(*args)

            cache_values[args] = result
            return result

    return inner
