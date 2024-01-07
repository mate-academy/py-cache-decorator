from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> dict:
        key = (args)

        if key in cached_results:
            print("Getting from cache")

        else:
            cached_results[key] = func(*args)
            print("Calculating new result")

        return cached_results[key]

    return wrapper
