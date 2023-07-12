from typing import Callable

def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args: Callable) -> Callable:
        if args in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[args] = result = func(*args)
        return cached_results
    return wrapper
