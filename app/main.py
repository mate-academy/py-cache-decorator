from typing import Callable, TypeVar
ReturnType = TypeVar("ReturnType")


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> ReturnType:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache_data.keys():
            cache_data[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_data[key]
    return wrapper
