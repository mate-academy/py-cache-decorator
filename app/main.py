from typing import Callable


def cache(func: Callable) -> Callable:
    runs_cache = {}

    def wrapper(*args) -> Callable:
        if args not in runs_cache.keys():
            runs_cache[args] = func(*args)
            print("Calculating new result")
            return runs_cache[args]
        else:
            print("Getting from cache")
            return runs_cache[args]

    return wrapper
