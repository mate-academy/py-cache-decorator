from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args: tuple) -> callable:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]

        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result
    return wrapper
