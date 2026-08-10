from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_data:
            cache_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_data[args]
    return wrapper
