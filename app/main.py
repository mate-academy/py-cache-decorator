from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args) -> Any:
        if args not in cached_result.keys():
            cached_result[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_result[args]

    return wrapper
