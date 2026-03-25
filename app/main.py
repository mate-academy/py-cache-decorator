from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> None:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        else:
            result = func(*args, **kwargs)
            cache_data[args] = result
            print("Calculating new result")
            return result
    return wrapper
