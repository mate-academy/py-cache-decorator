from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        id_func = (tuple(args) + tuple(kwargs.keys()))
        if id_func not in cache_dict:
            print("Calculating new result")
            cache_dict[id_func] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_dict[id_func]

    return wrapper
