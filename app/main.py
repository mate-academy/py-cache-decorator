from typing import Callable


def cache(func: Callable) -> Callable:
    cache_files = {}

    def wrapper(*args) -> None:
        if args not in cache_files:
            cache_files[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_files[args]
    return wrapper
