from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper
