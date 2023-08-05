from typing import Callable


def cache(func: Callable) -> Callable:

    result_cache = {}

    def wrapper(*args) -> None:
        if args in result_cache:
            print("Getting from cache")
            return result_cache[args]
        else:
            result_cache[args] = func(*args)
            print("Calculating new result")
            return result_cache[args]
    return wrapper
