from typing import Callable


def cache(func: Callable) -> Callable:
    cached_values = {}

    def inner(*args) -> int:
        cached_keys = args
        if cached_keys not in cached_values:
            print("Calculating new result")
            res = func(*args)
            cached_values[cached_keys] = res
            return res
        else:
            print("Getting from cache")
            return cached_values[cached_keys]

    return inner
