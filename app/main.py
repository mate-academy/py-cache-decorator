from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            res = func(*args)
            cache_dict[args] = res
        else:
            print("Getting from cache")
        return cache_dict[args]
    return wrapper
