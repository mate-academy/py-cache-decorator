from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_database = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        if args not in cache_database:
            print("Calculating new result")
            cache_database[args] = func(*args)
            return cache_database[args]

        print("Getting from cache")
        return cache_database[args]
    return wrapper
