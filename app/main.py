from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> int:
        cache_data
        if (args, tuple(kwargs.items())) in cache_data:
            print("Getting from cache")
            return cache_data[(args, tuple(kwargs.items()))]
        else:
            result = func(*args, **kwargs)
            cache_data[(args, tuple(kwargs.items()))] = result
            print("Calculating new result")
            return result

    return wrapper
