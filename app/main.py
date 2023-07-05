from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: None) -> None:
        if args in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
        return cache_dict[args]
    return wrapper
