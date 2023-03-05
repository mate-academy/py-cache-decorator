from typing import Callable


def cache(func: Callable) -> None:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> None:
        if args in cache_dict:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cache_dict[args] = func(*args, **kwargs)
        return cache_dict[args]
    return wrapper
