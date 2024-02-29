from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            result = cache_dict[key] if key in cache_dict \
                else cache_dict.setdefault(key, func(*args, **kwargs))
            print("Calculating new result")
        return result

    return wrapper
