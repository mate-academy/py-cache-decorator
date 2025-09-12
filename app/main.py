from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def wrapper(*args) -> Any:
        if args in cached_result:
            print("Getting from cache")
            return cached_result[args]
        else:
            print("Calculating new result")
            cached_result[args] = func(*args)
            return cached_result[args]
    return wrapper
