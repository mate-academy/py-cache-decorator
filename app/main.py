from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args) -> Any:
        if args in cache_result:
            print("Getting from cache")
        else:
            cache_result[args] = func(*args)
            print("Calculating new result")

        return cache_result[args]

    return wrapper
