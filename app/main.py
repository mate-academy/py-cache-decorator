from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> int:
        key = args
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_results[key] = result
            return result
    return wrapper
