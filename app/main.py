from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> None:
        tupl = (args, tuple(sorted(kwargs.items())))
        if tupl in cache_dict.keys():
            print("Getting from cache")
            return cache_dict[tupl]
        cache_dict[tupl] = func(*args, **kwargs)
        print("Calculating new result")
        return cache_dict[tupl]
    return wrapper
