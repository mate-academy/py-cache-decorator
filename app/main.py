from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))

        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]

        else:
            print("Calculating new result")
            key_local = (args, tuple(kwargs.items()))
            cache_data[key_local] = func(*args, **kwargs)

            return cache_data[key_local]

    return wrapper
