from typing import Callable


def cache(func: Callable) -> Callable:
    items_in_cached = {}

    def wrapper(*args) -> Callable:
        if args in items_in_cached.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            items_in_cached[args] = func(*args)
        return items_in_cached[args]
    return wrapper
