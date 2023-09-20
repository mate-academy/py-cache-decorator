from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> None:
        if args in cached_results:
            print("Getting from cache")
            return cached_results[args]
        else:
            print("Calculating new result")
            result = cached_results[args] = func(*args)
            return result
    return wrapper
