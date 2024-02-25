from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> Callable:
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]
        cached_data[args] = func(*args)
        print("Calculating new result")
        return cached_data[args]

    return wrapper
