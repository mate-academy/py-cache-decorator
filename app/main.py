from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args, **kwargs) -> Callable:
        key = (*args, *kwargs.items())

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            cache_storage[key] = res

            return res

    return inner
