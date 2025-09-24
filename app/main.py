from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        tuple_kwargs = tuple(
            [
                (key, value)
                for key, value in kwargs.items()
            ]
        )
        if (args, tuple_kwargs, func.__name__) in cache_dict:
            print("Getting from cache")
            return cache_dict[(args, tuple_kwargs, func.__name__)]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[(args, tuple_kwargs, func.__name__)] = result
            return result

    return wrapper
