from typing import Callable, Any
import functools


def make_key(args: Any, kwargs: Any) -> tuple:
    args_key = args
    kwargs_key = tuple(sorted(kwargs.items()))
    return args_key + kwargs_key


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        cache_key = make_key(args, kwargs)

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result
    return wrapper
