from typing import Callable, Any


def cache(func: Callable) -> Any:
    saved_cache = {}

    def inner(*args) -> Any:
        if args not in saved_cache:
            saved_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return saved_cache[args]

    return inner
