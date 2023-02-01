from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_dict = {}

    def wrapper(*args: int) -> Any:

        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[args]
    return wrapper
