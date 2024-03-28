from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args) -> int:
        for key in cached_results:
            if key == args:
                print("Getting from cache")
                return cached_results[key]
        result = func(*args)
        cached_results[args] = result
        print("Calculating new result")
        return result
    return wrapper
