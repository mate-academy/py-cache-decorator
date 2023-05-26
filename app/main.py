from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_value = {}

    def wrapper(*args) -> Any:
        if args in cache_value:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_value[args] = func(*args)
        return cache_value[args]
    return wrapper
