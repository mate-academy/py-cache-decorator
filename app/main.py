from typing import Callable


def cache(func: Callable) -> None:
    cache_data = {}

    def wrapper(*args, **kwargs) -> None:
        key = args + tuple(kwargs.values())
        if key not in cache_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[key] = result
        else:
            print("Getting from cache")

        return cache_data[key]

    return wrapper
