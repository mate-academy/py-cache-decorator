from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> None:
        if args in cache_dict:
            print("Getting from cache")
        if args not in cache_dict:
            print("Calculating new result")
            total = func(*args)
            cache_dict[args] = total
        return cache_dict[args]
    return wrapper
