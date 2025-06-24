from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data: dict = {}

    def wrapper(*args, **kwargs) -> int:
        key: tuple = (args, frozenset(kwargs.items()))

        if key in cached_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_data[key] = func(*args, **kwargs)

        return cached_data[key]
    return wrapper
