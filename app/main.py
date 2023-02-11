from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        arguments = *args, *kwargs.values()
        if arguments not in cache_dict:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[arguments] = result
            return result
        else:
            print("Getting from cache")
            return cache_dict[arguments]

    return wrapper
