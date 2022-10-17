from typing import Callable

def cache(func: Callable) -> Callable:
    cache_backet = {}

    def wrapper(*args):
        if args not in cache_backet:
            result = func(*args)
            cache_backet[args] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_backet[args]
    return wrapper
