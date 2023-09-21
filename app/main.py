from typing import Callable

cached_results = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Callable:
        key = (func, args, frozenset(kwargs.items()))

        if key not in cached_results:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
        else:
            print("Getting from cache")

        return cached_results[key]

    return wrapper
