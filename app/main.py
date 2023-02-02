from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> int:
        if args not in cached_data:
            result = func(*args)
            cached_data[args] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
            result = cached_data[args]
        return result

    return wrapper
