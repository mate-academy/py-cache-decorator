from typing import Callable

def cache(func: Callable) -> Callable:
    cached_result = {}
    def inner(*args) -> Callable:
        if args not in cached_result:
            cached_result[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_result[args]
    return inner