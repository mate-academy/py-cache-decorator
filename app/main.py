from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args) -> None:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        add = True
        for arg in args:
            if isinstance(arg, (list, set, dict)):
                add = False
        if add:
            cache_dict[args] = func(*args)
        return func(*args)

    return inner
