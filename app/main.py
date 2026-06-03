from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: object, **kwargs: object) -> object:
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache_dict:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_dict[key]
    return wrapper
