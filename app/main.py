from typing import Callable, Any
from functools import wraps


# Assigning global variable 'cache_dict' which we use for storing our cache.
# 'cache_dict' stores hash of functions as keys and another dictionaries
# as values.
# Internal dictionaries stores arguments of functions as keys and results of
# functions as values.
cache_dict = dict()


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> Any:
        # we use neither '__name__' nor 'id()'
        # because decorator actually caches previous tests.
        hash_of_function = func.__hash__

        if hash_of_function not in cache_dict:
            cache_dict[hash_of_function] = dict()

        if args not in cache_dict[hash_of_function]:
            cache_dict[hash_of_function][args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_dict[hash_of_function][args]

    return wrapper
