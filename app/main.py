from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args) -> str:
        data = tuple(args)

        if data in cache_data:
            print("Getting from cache")
            return cache_data[data]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_data[data] = result
            return result
    return wrapper
