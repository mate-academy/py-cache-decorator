from typing import Callable


def cache(func: Callable) -> Callable:
    new_cache = {}

    def wrapper(*args) -> Callable:
        if args in new_cache:
            print("Getting from cache")
            return new_cache[args]

        print("Calculating new result")
        result = func(*args)
        new_cache[args] = result
        return result

    return wrapper
