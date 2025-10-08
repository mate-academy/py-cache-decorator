from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = {}

    def wrapper(*args, **kwargs) -> Callable:
        caches_key = args
        if caches_key in cache_list:
            print("Getting from cache")
            return cache_list[caches_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_list[caches_key] = result
        return result
    return wrapper
