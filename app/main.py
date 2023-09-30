from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> int:
        if args in cache_dict:
            print("Getting from cache")
        else:
            new_result = func(*args)
            cache_dict[args] = new_result
            print("Calculating new result")
        return cache_dict[args]
    return wrapper
