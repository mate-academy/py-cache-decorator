from typing import Callable


def cache(func: Callable) -> Callable:
    some_cache = {}

    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))
        if key in some_cache:
            print("Getting from cache")
            return(some_cache[key])
        result = func(*args, **kwargs)
        some_cache[key] = result
        print("Calculating new result")
        return result
    return wrapper
