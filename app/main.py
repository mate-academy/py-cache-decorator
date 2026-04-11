from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @wraps(func)
    def inner(*args, **kwargs) -> None:
        key_func = (*args, tuple(sorted(kwargs.items())))
        if key_func in cache_dict:
            print("Getting from cache")
            return cache_dict[key_func]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key_func] = result
        return result

    return inner
