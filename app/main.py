from typing import Callable


def cache(func: Callable) -> Callable:

    cache_or_no = {}
    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_or_no:
            print("Getting from cache")
            return cache_or_no[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_or_no[key] = result
            return result
    return wrapper


