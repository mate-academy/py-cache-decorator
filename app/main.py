from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args: Any, **kwargs) -> Callable:
        key = args
        if key not in cache_dict:
            print("Calculating new result")
            value = func(*args, **kwargs)
            cache_dict[key] = value
            result = value
        else:
            print("Getting from cache")
            result = cache_dict[key]
        return result
    return inner
