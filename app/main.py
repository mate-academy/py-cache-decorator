from typing import Callable


def cache(func: Callable) -> Callable:
    data_cache = {}

    def wrapper(*args, **kwargs) -> Callable:

        if args not in data_cache:
            print("Calculating new result")
            data_cache[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return data_cache[args]
    return wrapper
