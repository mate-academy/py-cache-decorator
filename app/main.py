from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def wrapper(*args, **kwargs) -> int:
        key = str((args, kwargs))

        if key not in cache_dictionary:
            print("Calculating new result")
            cache_dictionary[key] = func(*args, **kwargs)
            return cache_dictionary[key]
        print("Getting from cache")
        return cache_dictionary[key]
    return wrapper
