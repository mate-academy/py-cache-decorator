from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
            return cache_dict[key]
    return wrapper


# I wrote a new function because I deleted the old one
@cache
def expensive_function(param1: int, param2: int) -> int:
    return param1 + param2


@cache
def another_expensive_function(arg1: int, arg2: int, arg3: int) -> int:
    return arg1 * arg2 * arg3
