from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args, **kwargs) -> str:
        key = (args, frozenset(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        result = func(*args, **kwargs)
        cached_results[key] = result
        print("Calculating new result")
        return result
    return inner
