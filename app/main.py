from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        data = (args, tuple(kwargs.items()))

        if data in cache_dict:
            print("Getting from cache")
            return cache_dict[data]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[data] = result

        return result

    return wrapper
