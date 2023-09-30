from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper


@cache
def expensive_function(param1: int, param2: int) -> int:
    return param1 + param2


def another_expensive_function(arg1: int, arg2: int, arg3: int) -> int:
    return arg1 * arg2 * arg3
