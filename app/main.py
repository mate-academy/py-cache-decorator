from typing import Callable

def cache(func: Callable) -> Callable:
    cache_value = {}

    def inner(*args):
        if cache_value.get(args) is None:
            print("Calculating new result")
            cache_value[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_value[args]

    return inner