from typing import Callable


def cache(func: Callable) -> Callable:
    cache_1 = {}

    def wrapper(*args, **kwargs) -> None:
        result = (args, tuple(sorted(kwargs.items())))
        if result not in cache_1:
            print("Calculating new result")
            cache_1[result] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_1[result]
    return wrapper
