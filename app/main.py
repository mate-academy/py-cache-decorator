from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[key]

    return wrapper
