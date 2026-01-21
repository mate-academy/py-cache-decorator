from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if func not in cache_dict:
            cache_dict[func] = {}
        if key in cache_dict[func]:
            print("Getting from cache")
            return cache_dict[func][key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[func][key] = result
        return result
    return wrapper
