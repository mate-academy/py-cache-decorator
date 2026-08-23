from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def inner(*args, **kwargs) -> int:
        key = (args, tuple(kwargs.items()))
        if key in cache:
            print("Getting from cache")
            return cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return inner
