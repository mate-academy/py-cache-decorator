from typing import Callable


def cache(func: Callable) -> Callable:
    cashed_items = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cashed_items:
            result = func(*args, **kwargs)
            cashed_items[key] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cashed_items[key]
    return wrapper
