from typing import Callable


def cache(func: Callable, cached_results: {} = None) -> Callable:
    if cached_results is None:
        cached_results = {}

    def wrapper(*args) -> None:
        if args not in cached_results:
            print("Calculating new result")
            cached_results[args] = func(*args)
        else:
            print("Getting from cache")
        return cached_results[args]

    return wrapper
