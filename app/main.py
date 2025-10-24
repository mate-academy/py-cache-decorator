from typing import Callable


def cache(func: Callable) -> Callable:
    cache_box = {}  # for cache

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in cache_box:
            print("Getting from cache")
            return cache_box[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_box[key] = result  # save to cache for reuse
            return result

    return wrapper