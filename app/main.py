from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> dict:
        key = (args)

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        else:
            result = func(*args)
            cached_results[key] = result
            print("Calculating new result")
            return result

    return wrapper
