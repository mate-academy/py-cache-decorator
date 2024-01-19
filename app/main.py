from typing import Callable


def cache(func: Callable) -> Callable:
    saved_result = {}

    def wrapper_cache(*args) -> dict:
        if args in saved_result:
            print("Getting from cache")
            return saved_result[args]
        else:
            print("Calculating new result")
            saved_result[args] = func(*args)
            return saved_result[args]

    return wrapper_cache
