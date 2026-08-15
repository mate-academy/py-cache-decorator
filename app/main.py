from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
            return cache_dict[args]

    return wrapper
