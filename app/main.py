from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> int:
        if args in cached_results:
            print("Getting from cache")
        else:
            cached_results[args] = func(*args)
            print("Calculating new result")
        return cached_results[args]

    return wrapper
