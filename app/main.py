from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
        else:
            print("Getting from cache")
        return cache_dict[args]
    return wrapper
