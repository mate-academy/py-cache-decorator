from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args) -> Any:
        if args in cache_results:
            print("Getting from cache")
            return cache_results[args]
        else:
            print("Calculating new result")
            cache_results[args] = func(*args)
            return cache_results[args]
    return wrapper
