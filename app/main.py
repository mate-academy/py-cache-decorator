from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrappers(*args) -> Callable:
        if args not in cache_results:
            cache_results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_results[args]
    return wrappers
