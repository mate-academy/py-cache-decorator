from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> int:
        if args not in cached_data:
            cached_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cached_data[args]

    return wrapper
