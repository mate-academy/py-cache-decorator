from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {} # I want to create dict

    def wrapper (*args):

        key = (func.__name__, args)

        # Check if the result is already in the cache
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        # If not in cache, calculate the result and store it
        print("Calculating new result")
        result = func(*args)
        cache_dict[key] = result
        return result

    return wrapper
