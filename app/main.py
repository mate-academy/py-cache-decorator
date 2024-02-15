from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> None:
        if args not in cached_results:
            cached_results[args] = func(*args)
            print("Calculating new result")
            return cached_results[args]
        else:
            print("Getting from cache")
            return cached_results[args]

    return wrapper
