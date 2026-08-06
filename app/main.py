from typing import Callable


def cache(func: Callable) -> Callable:

    cache_store = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]

        print("Calculating new result")
        value = func(*args, **kwargs)
        cache_store[key] = value

        return value

    return wrapper
