from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args, **kwargs) -> Any:

        if args in cache_result:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_result[args] = func(*args, **kwargs)
        return cache_result[args]

    return wrapper
