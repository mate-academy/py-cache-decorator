from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> int | list[int]:
        if cache_dict.get(args) is None:
            result = func(*args, **kwargs)
            cache_dict[args] = result
            print("Calculating new result")
        else:
            result = cache_dict[args]
            print("Getting from cache")
        return result

    return inner
