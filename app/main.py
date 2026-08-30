from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_items = dict()

    def inner(*args) -> Any:
        if args not in cached_items:
            print("Calculating new result")
            cached_items[args] = func(*args)
        else:
            print("Getting from cache")
        return cached_items[args]

    return inner
