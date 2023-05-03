from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in dict_cache:
            print("Getting from cache")
            return dict_cache[args]
        else:
            print("Calculating new result")
            dict_cache[args] = func(*args, **kwargs)
            return dict_cache[args]

    return wrapper
