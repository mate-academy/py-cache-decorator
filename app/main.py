from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:

        cache_key = args + tuple(sorted(kwargs.items()))
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            print("Calculating new result")
            return result

    return wrapper
