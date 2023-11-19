from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_dictionary = {}

    @wraps(func)
    def wrapper(*args) -> any:
        if args in cache_dictionary.keys():
            print("Getting from cache")
            return cache_dictionary[args]

        print("Calculating new result")
        cache_dictionary[args] = func(*args)
        return cache_dictionary[args]

    return wrapper
