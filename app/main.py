from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in cache:
            print("Getting from cache")
            return cache[key]
        result_of_func = func(*args, **kwargs)
        cache[key] = result_of_func
        print("Calculating new result")
        return result_of_func
    return wrapper
