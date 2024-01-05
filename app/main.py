from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> None:
        cache_key = (func.__name__, args, frozenset(kwargs.items()))

        if cache_key in cached_results:
            print("Getting from cache")
            return cached_results[cache_key]

        result = func(*args, **kwargs)
        print("Calculating new result")
        cached_results[cache_key] = result
        return result

    return wrapper
