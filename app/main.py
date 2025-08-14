from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args) -> tuple:
        if args in cache_results:
            print("Getting from cache")
            result = cache_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_results[args] = result
        return result
    return wrapper
