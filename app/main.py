from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        tupl = (args, tuple(sorted(kwargs.items())))
        if tupl in cache_dict.keys():
            print("Getting from cache")
            return cache_dict[tupl]
        print("Calculating new result")
        cache_dict[tupl] = func(*args, **kwargs)
        return cache_dict[tupl]
    return wrapper
