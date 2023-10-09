from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args) -> Callable:
        cache_key = (args)
        if cache_key in cache_result.keys():
            print("Getting from cache")
        else:
            cache_result[cache_key] = func(*args)
            print("Calculating new result")
        return cache_result[cache_key]
    return wrapper
    pass
