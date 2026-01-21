from typing import Callable


def cache(func: Callable) -> Callable:
    my_cache = {}

    def wrapper(*args) -> Callable:
        if args not in my_cache:
            print("Calculating new result")
            result = func(*args)
            my_cache[args] = result
            return result
        else:
            print("Getting from cache")
            return my_cache[args]
    return wrapper
