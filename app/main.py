from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_dict[key]
        else:
            print("Getting from cache")
            return cache_dict[key]

    return inner
